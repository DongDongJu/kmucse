/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

namespace BerkeleyDB.Internal {

using System;
using System.Runtime.InteropServices;

internal class DB_LOCK : IDisposable {
  private HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal DB_LOCK(IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new HandleRef(this, cPtr);
  }

  internal static HandleRef getCPtr(DB_LOCK obj) {
    return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
  }

  ~DB_LOCK() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          libdb_csharpPINVOKE.delete_DB_LOCK(swigCPtr);
        }
        swigCPtr = new HandleRef(null, IntPtr.Zero);
      }
      GC.SuppressFinalize(this);
    }
  }

  internal uint off {
    set {
      libdb_csharpPINVOKE.DB_LOCK_off_set(swigCPtr, value);
    } 
    get {
      uint ret = libdb_csharpPINVOKE.DB_LOCK_off_get(swigCPtr);
      return ret;
    } 
  }

  internal uint ndx {
    set {
      libdb_csharpPINVOKE.DB_LOCK_ndx_set(swigCPtr, value);
    } 
    get {
      uint ret = libdb_csharpPINVOKE.DB_LOCK_ndx_get(swigCPtr);
      return ret;
    } 
  }

  internal uint gen {
    set {
      libdb_csharpPINVOKE.DB_LOCK_gen_set(swigCPtr, value);
    } 
    get {
      uint ret = libdb_csharpPINVOKE.DB_LOCK_gen_get(swigCPtr);
      return ret;
    } 
  }

  internal db_lockmode_t mode {
    set {
      libdb_csharpPINVOKE.DB_LOCK_mode_set(swigCPtr, (int)value);
    } 
    get {
      db_lockmode_t ret = (db_lockmode_t)libdb_csharpPINVOKE.DB_LOCK_mode_get(swigCPtr);
      return ret;
    } 
  }

  internal DB_LOCK() : this(libdb_csharpPINVOKE.new_DB_LOCK(), true) {
  }

}

}
