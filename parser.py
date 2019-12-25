class DNA:

    def __init__(self, identifier, instrument, run_number, flowcell_ID, lane, title, x_pos, y_pos, read, is_filtered, control, index_sequence):
        self.instrument = instrument
        self. run_number = run_number
        self.flowcell_ID = flowcell_ID
        self.lane = lane
        self.title = title
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.read = read
        self.is_filtered = is_filtered
        self.control = control
        self.index_sequence = index_sequence


sample1 = DNA('@HFG-SDFS', 'fsdf', 'Y', 'dfsds', 'sdfs', 'sdf', 'sdfs', 'sdfs', 'sdfs', 'sdf', 'sdf')

print(sample1.y_pos)