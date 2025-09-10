`ifndef UART_AGENT_SV
`define UART_AGENT_SV

class uart_agent extends uvm_agent;
  `uvm_component_utils(uart_agent)

  uart_driver m_driver;
  uart_monitor m_monitor;
  uvm_sequencer #(uart_seq_item) m_seqr;
  virtual uart_if vif;
  uvm_active_passive_enum m_active = UVM_ACTIVE;

  function new(string name = "uart_agent", uvm_component parent = null);
    super.new(name,parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if (m_active == UVM_ACTIVE) begin
      m_driver = uart_driver::type_id::create("m_driver", this);
      m_seqr = uvm_sequencer#(uart_seq_item)::type_id::create("m_seqr", this);
    end
    m_monitor = uart_monitor::type_id::create("m_monitor", this);
  endfunction

  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    if (!uvm_config_db#(virtual uart_if)::get(this, "", "uart_if", vif)) begin
      `uvm_fatal(get_type_name(), "cannot access the interface")
    end
     else begin
      `uvm_info("AGT", "able to access the interface", UVM_LOW)
    end

    if (m_active == UVM_ACTIVE) begin
      m_driver.vif = vif;
      m_driver.seq_item_port.connect(m_seqr.seq_item_export);
       `uvm_info("AGT","connected m_drv.seq_item_port -> m_seqr.seq_item_export", UVM_LOW)
    end
    m_monitor.vif = vif;
  endfunction

endclass

`endif
