`ifndef {name_upper}_AGENT_SV
`define {name_upper}_AGENT_SV

class {name}_agent extends uvm_agent;
  `uvm_component_utils({name}_agent)

  {name}_driver m_driver;
  {name}_monitor m_monitor;
  uvm_sequencer #({name}_seq_item) m_seqr;
  virtual {name}_if vif;
  uvm_active_passive_enum m_active = UVM_ACTIVE;

  function new(string name = "{name}_agent", uvm_component parent = null);
    super.new(name,parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if (m_active == UVM_ACTIVE) begin
      m_driver = {name}_driver::type_id::create("m_driver", this);
      m_seqr = uvm_sequencer#({name}_seq_item)::type_id::create("m_seqr", this);
    end
    m_monitor = {name}_monitor::type_id::create("m_monitor", this);
  endfunction

  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    if (!uvm_config_db#(virtual {name}_if)::get(this, "", "{name}_if", vif)) begin
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
