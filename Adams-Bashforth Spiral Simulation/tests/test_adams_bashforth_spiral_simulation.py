import os
import numpy as np
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.adams_bashforth_spiral_simulation import ab_spiral

def test_ab_spiral():
    Dt = 0.1
    n = 10
    output_file = os.path.join(os.path.dirname(__file__), '..', 'src', 'output.txt')
    
    # Run the simulation
    ab_spiral(Dt, n)
    
    # Check if the output file is created
    assert os.path.exists(output_file)
    
    # Read the output file and check its contents
    with open(output_file, 'r') as f:
        lines = f.readlines()
        assert len(lines) == n + 1  # Check if the number of lines is correct
        
        # Check the format of the first line
        first_line = lines[0].strip().split()
        assert len(first_line) == 3  # Should have three columns: t, x, y
        assert float(first_line[0]) == 0.0  # Initial time should be 0.0
        assert float(first_line[1]) == 1.0  # Initial x position
        assert float(first_line[2]) == 0.0  # Initial y position
    
    # Clean up: delete the output file
    os.remove(output_file)

if __name__ == "__main__":
    pytest.main()