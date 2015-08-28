''' Copyright (c) 2015 Potential Ventures Ltd
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of Potential Ventures Ltd
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL POTENTIAL VENTURES LTD BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. '''

import logging

import cocotb
from cocotb.handle import HierarchyObject, ModifiableObject, RealObject, IntegerObject, ConstantObject
from cocotb.triggers import Timer
from cocotb.result import TestError, TestFailure




@cocotb.test()
def check_objects(dut):
    """
    Check the types of objects that are returned
    """
    tlog = logging.getLogger("cocotb.test")
    fails = 0
    yield Timer(100)

    def check_instance(obj, objtype):
        if not isinstance(obj, objtype):
            tlog.error("Expected %s to be of type %s but got %s" % (
                obj._fullname, objtype.__name__, obj.__class__.__name__))
            return 1
        tlog.info("%s is %s" % (obj._fullname, obj.__class__.__name__))
        return 0

    # Hierarchy checks
    fails += check_instance(dut.inst_axi4s_buffer, HierarchyObject)
    fails += check_instance(dut.gen_branch_distance[0], HierarchyObject)
    fails += check_instance(dut.gen_branch_distance[0].inst_branch_distance, HierarchyObject)
    fails += check_instance(dut.gen_acs[0].inbranch_tdata_low, ModifiableObject)
    fails += check_instance(dut.gen_acs[0].inbranch_tdata_low[0], ModifiableObject)

    fails += check_instance(dut.aclk, ModifiableObject)
    fails += check_instance(dut.s_axis_input_tdata, ModifiableObject)

    fails += check_instance(dut.current_active, IntegerObject)

    fails += check_instance(dut.inst_axi4s_buffer.DATA_WIDTH, ConstantObject)

    if fails:
        raise TestFailure("%d objects were not of the expected type" % fails)


