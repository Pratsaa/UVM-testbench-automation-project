# Paths for the memory and FIFO generation
MEMORY_RTL_PATH = ../../../../common/ip/dl_mem/rtl
FIFO_RTL_PATH   = ../../../../common/ip/dl_fifo/rtl

# Memory and FIFO generation commands
MEM_GEN_CMD = vpl2sv --vpl mem_wrap_a1r1w.vpl --sv sample_mem_async_wrap.sv MEM_NAME="sample_mem_async" DEPTH=16 DATA_WIDTH=32 ECC=0 PIPE_PRE_ECC_GEN=0 PIPE_ECC_GEN=0 PIPE_POST_ECC_GEN=0 PIPE_PRE_ECC_CHK=0 PIPE_ECC_CHK=0 PIPE_POST_ECC_CHK=0 PIPE_MEM_IN=0 PIPE_MEM_OUT=0 VENDOR_MEM_TYPE="sagslslg4u1p" FPGA_MEM_TYPE="uram"

FIFO_GEN_CMD = vpl2sv --vpl dl_async_fifo_ft.vpl --sv dl_async_fifo_ft_wrapper.sv MODULE_NAME="dl_async_fifo_ft_wrapper" MEM_WRAPPER_NAME="sample_mem_async_wrap" MEM_TYPE="_1r1w" MEM_RD_LATENCY=0 DEPTH=16 DATA_WIDTH=32 ECC=0 VENDOR_MEM_TYPE="xyz" FULL_RESET_VALUE=0 EARLY_FULL_VALUE=15 EARLY_EMPTY_VALUE=1 FPGA_MEM_TYPE="xyz"

# Default target
generate_design:
	@echo "Generating Memory and FIFO..."
	cd $(MEMORY_RTL_PATH) && $(MEM_GEN_CMD)
	cd $(FIFO_RTL_PATH) && $(FIFO_GEN_CMD)
	@echo "Compilation complete."

clean_design:
	@echo "Cleaning up existing design files..."
	@rm -rf $(MEMORY_RTL_PATH)/sample_mem_wrap.sv
	@rm -rf $(FIFO_RTL_PATH)/dl_sync_fifo_ft_wrapper.sv
	@echo "Design files removed."

# Overriding PRE_ANALYZE target
override PRE_ANALYZE = $(MAKE) clean_design && $(MAKE) generate_design

EXTRA_CMPARGS   += 
EXTRA_CMPARGS   += 
EXTRA_RUNARGS   += 

VHDL_ANA_ARGS   += 
VLOG_ANA_ARGS   += -sv_net_ports=packed +define+USE_BEH_MEM
CMP_ARGS        += -sv_net_ports=packed -timescale=1ns/1ps

RUN_ARGS        += 

TB_PRE_RUN       += echo "No TB_PRE_RUN" 

#Modify the following line with the relative path to the Makefile
include ../../../common/vip/misc/Makefile.inc
