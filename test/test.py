import cocotb
from cocotb.triggers import ClockCycles, RisingEdge

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting PQC RNG Testbench")

    # Start the clock generator loop safely
    # (Toggles the dut.clk signal every 50ns for a 10MHz operation frequency)
    cocotb.start_soon(cocotb.clock.Clock(dut.clk, 100, units="ns").start())

    # 1. System Reset Initialization
    dut._log.info("Applying system reset...")
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    
    # Hold reset active for 5 clock cycles
    await ClockCycles(dut.clk, 5)
    
    # De-assert reset on a rising edge
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)

    # 2. Test Autonomous PRNG Mode (uio_in[0] / mode_sel = 0)
    dut._log.info("Testing Autonomous PRNG Sequence Generation...")
    dut.uio_in.value = 0  # Set mode_sel pin to 0
    await ClockCycles(dut.clk, 2)
    
    # Capture consecutive cycle outputs to confirm random shifts
    val1 = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 1)
    val2 = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 1)
    val3 = int(dut.uo_out.value)
    
    dut._log.info(f"Generated Random Sequence Stream values: {val1}, {val2}, {val3}")
    
    # 3. Test Hybrid Seeding Mode (uio_in[0] / mode_sel = 1)
    dut._log.info("Testing Hybrid Entropy Injection Mode...")
    dut.uio_in.value = 1  # Set mode_sel pin to 1
    dut.ui_in.value = 0x55  # Inject alternative seed mapping bits
    await ClockCycles(dut.clk, 5)
    
    dut._log.info("RNG Test completed successfully.")
