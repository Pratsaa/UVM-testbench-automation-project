+incdir+../../../../../common/vip/clock_controller
+incdir+../../../../../common/vip/misc
+incdir+../../tb
+incdir+../../tb/alu_agent
+incdir+../../tb/dma_agent
+incdir+../../tb/uart_agent
+incdir+../../tests
+define++UVM_PACKER_MAX_BYTES=10000
+define+UVM_DISABLE_AUTO_ITEM_RECORDING
+incdir+${VCS_HOME}/etc/uvm-ieee-2020/vcs
+incdir+../../../../common/ip/dl_misc/rtl
+incdir+../../../../common/ip/dl_fifo/rtl
//Add directories to the relevant files over here

-y ../../../../common/ip/dl_misc/rtl
-y ../../../../common/ip/dl_fifo/rtl
//Add directories to the relevant files over here

+incdir+../../../../common/vip/src/
-y ../../../../common/vip/src/
+incdir+../../tests/dl_async_fifo_ft_test
+incdir+${VCS_HOME}/etc/uvm-ieee-2020/vcs
+incdir+${VCS_HOME}/etc/uvm-ieee-2020/verdi
-y ../../tests
-y ../../../../common/vip/

${VCS_HOME}/etc/uvm-ieee-2020/uvm_pkg.sv
${VCS_HOME}/etc/uvm-ieee-2020/vcs/uvm_custom_install_vcs_recorder.sv
${VCS_HOME}/etc/uvm-ieee-2020/verdi/uvm_custom_install_verdi_recorder.sv

../../tb/alu_agent/alu_if.sv
../../tb/dma_agent/dma_if.sv
../../tb/uart_agent/uart_if.sv
//../../../../../common/vip/misc/clk_if.sv
../../tb/alu_agent/alu_agent_pkg.sv
../../tb/dma_agent/dma_agent_pkg.sv
../../tb/uart_agent/uart_agent_pkg.sv
../../tb/tb_pkg.sv
../../tb/tb_top.sv
../../tb/finaltest1_harness.sv