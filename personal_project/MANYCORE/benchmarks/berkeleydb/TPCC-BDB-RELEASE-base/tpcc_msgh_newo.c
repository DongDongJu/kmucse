/*
 * Copyright (c) 2002 Harvard University - Alexandra Fedorova
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *      This product includes software developed by Harvard University
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

/* This file contains the implementation of the NEWORDER transaction
 * server. This server is forked by the inetd upon arrival of a
 * request from a benchmark client on a known port. 
 */

/*
#include <sys/types.h>
#include <sys/uio.h>

#include "db.h"
*/

#include <stdio.h>
#include <errno.h>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>


#include "msgh.h" 
#include "log.h"
#include "msgh_common.h"


double
get_delta_ms(struct timeval *before, struct timeval *after)
{
    double retval = 0;
    long diff_sec = 0, diff_usec = 0;

    if(before == NULL || after == NULL)
    {
	return -1000000;
    }

    diff_sec = after->tv_sec - before->tv_sec;
    
    if( (diff_usec = after->tv_usec - before->tv_usec) < 0)
    {
	if(diff_sec <= 0)
	{
	    fprintf(stderr, "Invalid input\n");
	}
	diff_sec--;
	diff_usec += 1000000;
    }
    
    retval = (double)diff_sec * (double)1000 + (double)diff_usec/(double)1000;

    return retval;
}

int mypid;

struct 
{
    struct msgh_req hdr;
    NEWORDER_TRANSACTION_DATA newomsg;
}message;

int 
main(int argc, char **argv)
{
    int len, tret;
    static int errcnt = 0;
    static int W_ID = 1;
    static int D_ID = 1;
    struct timeval before, after;
    double tx_time;
    int chkpt = 0;
    
    mypid = getpid();

       
    signal(SIGINT, SIG_IGN);
    signal(SIGQUIT, SIG_IGN);
    signal(SIGTERM, SIG_IGN);
    signal(SIGHUP,  SIG_IGN);

    if(init_log(mypid))
    {
	exit(1);
    }

    if(prepare_for_xactions("/dafsmnt", 0))
    {
	write_log("NEWO %d: could not prepare for transactions\n", 
		  mypid);
	exit(1);
    }
    
    write_log("NEWO %d: is up\n", mypid);
    
    /* Send ack back to message server */
    write(1, "I'm ready", 10);
    
    /* Main loop: read request, do transaction and send result back */
    
    while(1)
    {
	if((len = read(0, &message, sizeof(message))) <= 0)
	{
	    write_log
		("NEWO %d: read message failed: errno = %d\n",
		 mypid, errno);
	    if(++errcnt > 10)
	    {
		write_log
		    ("NEWO %d: too many errors, exiting\n", mypid);
		break;
	    }
	    else
		continue;
	}
	ntoh_msg_header(&message.hdr);
	if(len != sizeof(message))
	{
	    if(message.hdr.type == MSGH_SHUT)
	    {
		write_log("NEWO %d: shutting down\n", mypid);
		break;
	    }
	    write_log("NEWO %d: read %d, expected %d bytes\n", mypid, 
		      len, sizeof(message));
	    message.hdr.type = FAIL;
	    goto ret;
	}

	ntoh_neworder(&message.newomsg);
	/*
	if(gettimeofday(&before, 0))
	{
	    write_log("gtod failed\n");
	    break;
	}*/
	tret = do_neworder(&message.newomsg);
	/*
	if(gettimeofday(&after, 0))
	{
	    write_log("gtod failed\n");
	    break;
	}
	tx_time = get_delta_ms(&before, &after);*/
	write_log("NEWO %d: tx_time is %f\n", mypid, tx_time);

	if(tret)
	{
	    message.hdr.type = FAIL;
#if PRINT_TX_STATUS
	    write_log("NEWO %d: TRANSACTION FAILED\n", mypid);
#endif
	    hton_neworder(&message.newomsg);
	}
	else
	{
	    message.hdr.type = SUCCESS;
#if PRINT_TX_STATUS
	    write_log("NEWO %d: TRANSACTION SUCCEEDED\n", mypid);
#endif
	    hton_neworder(&message.newomsg);
	}
    ret:
	hton_msg_header(&message.hdr);	
	if(write(1, &message, sizeof(message)) <= 0)
	{
	    write_log("NEWO %d: write message failed, errno = %d\n", 
		      mypid, errno);
	    if(++errcnt > 10)
	    {
		("NEWO %d: too many errors, exiting\n", mypid);
		break;
	    }
	}
    }
    
    cleanup();
    exit(1);
}
