''' Copyright (c) 2013 Potential Ventures Ltd
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of Potential Ventures Ltd nor the
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
"""
Drivers for Solarflare bus format.

A specialisation of the AvalonST bus
"""
from cocotb.decorators import coroutine
from cocotb.triggers import RisingEdge

from cocotb.drivers.avalon import AvalonSTPkts


class SFStreaming(AvalonSTPkts):
    """This is the Solarflare Streaming bus as defined by the Solarflare FDK.

    Expect to see a 72-bit bus (bottom 64 bits data, top 8 bits are ECC)
    """
    _signals = ["valid", "data", "startofpacket", "endofpacket", "ready", "empty", "channel", "error"]

    def __init__(self, *args, **kwargs):
        AvalonSTPkts.__init__(self, *args, **kwargs)

        # Drive some sensible defaults onto the bus
        self.bus.startofpacket <= 0
        self.bus.endofpacket   <= 0
        self.bus.valid         <= 0
        self.bus.empty         <= 0
        self.bus.channel       <= 0
        self.bus.error         <= 0

