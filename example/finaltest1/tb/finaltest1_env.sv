`ifndef FINALTEST1_ENV_SV
`define FINALTEST1_ENV_SV

class finaltest1_env extends uvm_env;
  `uvm_component_utils(finaltest1_env)

  alu_agent m_alu_agent;
  dma_agent m_dma_agent;
  uart_agent m_uart_agent;
 // finaltest1_scoreboard m_scoreboard;

  function new(string name = "finaltest1_env", uvm_component parent = null);
    super.new(name, parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    m_alu_agent = alu_agent::type_id::create("m_alu_agent", this);
    m_dma_agent = dma_agent::type_id::create("m_dma_agent", this);
    m_uart_agent = uart_agent::type_id::create("m_uart_agent", this);
    //m_scoreboard = finaltest1_scoreboard::type_id::create("m_scoreboard", this);
  endfunction

  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    //m_alu_agent.m_monitor.ap.connect(m_scoreboard.alu_export);
    //m_dma_agent.m_monitor.ap.connect(m_scoreboard.dma_export);
    //m_uart_agent.m_monitor.ap.connect(m_scoreboard.uart_export);
  endfunction

endclass

`endif
