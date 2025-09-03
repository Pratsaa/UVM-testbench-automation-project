def generate_design_f() -> str:
    return """\
//Modify these directories as per your project structure
+libext+.sv+.v
+incdir+../../../../common/ip/dl_mem/rtl
+incdir+../../../../common/ip/dl_fifo/rtl
+incdir+../../../../common/ip/dl_regs/rtl
+incdir+../../../../common/ip/dl_misc/rtl
+incdir+./

//TODO: Modify the relative path to your design file in the following line
../../../../common/ip/dl_misc/rtl/dl_clk_freq.sv
"""