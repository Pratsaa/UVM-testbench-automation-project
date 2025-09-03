def generate_test_sv(module_name: str, interfaces: list) -> str:
    """
    Generate a UVM test file with basic test logic, supporting sequence overrides.

    Args:
        module_name (str): e.g., "pratyush2test"
        interfaces (list): list of dictionaries, each with a 'name' key, e.g., [{'name': 'alu'}, {'name': 'dma'}]
    """
    upper = module_name.upper()
    first_iface = interfaces[0]["name"] if interfaces else "agent"  # fallback in case list is empty

    return f'''\
`ifndef {upper}_TEST_SV
`define {upper}_TEST_SV

class {module_name}_test extends uvm_test;
  `uvm_component_utils({module_name}_test)

  {module_name}_env m_env;
  {module_name}_basic_seq base_seq;

  function new(string name = "{module_name}_test", uvm_component parent = null);
    super.new(name, parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    string test_seq_name;
    uvm_factory factory = uvm_factory::get();
    super.build_phase(phase);

    if($value$plusargs("sim_test_seq_name=%0s", test_seq_name)) begin
      `uvm_info(get_type_name(), $sformatf("Overriding tb_base_sequence with %0s", test_seq_name), UVM_LOW)
      factory.set_type_override_by_name("tb_basic_seq", test_seq_name);
    end
    m_env = {module_name}_env::type_id::create("m_env", this);
  endfunction

  virtual task run_phase(uvm_phase phase);
    phase.raise_objection(this);

    // Run the main test sequence
    base_seq = {module_name}_basic_seq::type_id::create("base_seq");
    base_seq.start(m_env.m_{first_iface}_agent.m_seqr);

    #100;
    phase.drop_objection(this);
  endtask

endclass

`endif
'''
