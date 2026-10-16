# compatibility_selftests.py
"""
This module provides unit tests for all compatibility checking
functions in compatibility.py, organized by equivalence partitions.
"""

import unittest
from compatibility import (
    get_component_specs,
    check_cpu_with_component,
    check_case_with_component,
    check_motherboard_with_component,
    check_cooler_with_component,
    check_gpu_with_component,
    check_psu_with_component,
    check_ram_with_component,
    calculate_cpu_compatibility,
    calculate_case_compatibility,
    calculate_motherboard_compatibility,
    calculate_cooler_compatibility,
    calculate_gpu_compatibility,
    calculate_psu_compatibility,
    calculate_ram_compatibility
)

class TestGetComponentSpecs(unittest.TestCase):
    """
    Test cases for get_component_specs function.
    
    Tests are organized by equivalence partitions
    
    Equivalence Partitions Tested:
        Valid partitions:
            - Component with valid specs dictionary
            - Component with empty specs dictionary
        Invalid partitions:
            - None input
            - Component missing 'specs' key
            - Empty component dictionary
    """
    
    def setUp(self):
        """Set up test data before each test case."""
        self.valid_component = {"name": "CPU", "specs": {"socket": "LGA1700", "tdp": 125}}
        self.empty_specs = {"name": "CPU", "specs": {}}
        self.no_specs_key = {"name": "CPU"}
        self.empty_component = {}
        self.none_input = None
    
    def test_valid_component_with_specs(self):
        """Test valid partition: component with specs dictionary."""
        result = get_component_specs(self.valid_component)
        self.assertEqual(result, {"socket": "LGA1700", "tdp": 125})
    
    def test_component_with_empty_specs(self):
        """Test valid partition: component with empty specs dictionary."""
        result = get_component_specs(self.empty_specs)
        self.assertEqual(result, {})
    
    def test_component_missing_specs_key(self):
        """Test invalid partition: component missing 'specs' key."""
        result = get_component_specs(self.no_specs_key)
        self.assertEqual(result, {})
    
    def test_empty_component(self):
        """Test invalid partition: empty component dictionary."""
        result = get_component_specs(self.empty_component)
        self.assertEqual(result, {})
    
    def test_none_input(self):
        """Test invalid partition: None input."""
        result = get_component_specs(self.none_input)
        self.assertEqual(result, {})

class TestCheckCPUWithComponent(unittest.TestCase):
    """
    Test cases for check_cpu_with_component function.
    
    Tests are organized by component type (motherboard, cooler, ram)
    
    Equivalence Partitions Tested - Motherboard:
        Valid: 
            - Matching sockets
        Invalid: 
            - Different sockets
            - Missing socket specs
    
    Equivalence Partitions Tested - Cooler:
        Valid: 
            - Socket compatible + sufficient TDP
            - No socket list assumed as valid
        Invalid: 
            - Socket incompatible
            - Insufficient TDP
    
    Equivalence Partitions Tested - RAM:
        Valid: 
            - Supported RAM type + capacity within limit
        Invalid: 
            - Unsupported RAM type
            - Capacity exceeded
    """
    
    def setUp(self):
        """Set up test data for CPU compatibility checks."""
        # CPU specs
        self.cpu_lga1700 = {"socket": "LGA1700", "tdp_rating": 125}
        self.cpu_am5 = {"socket": "AM5", "tdp_rating": 105}
        self.cpu_high_tdp = {"socket": "LGA1700", "tdp_rating": 250}
        
        # Motherboard specs
        self.mobo_lga1700 = {"socket": "LGA1700"}
        self.mobo_am5 = {"socket": "AM5"}
        self.mobo_no_socket = {}
        
        # Cooler specs
        self.cooler_compatible = {
            "socket_compatibility": ["LGA1700", "AM5"],
            "tdp_rating": 150
        }
        self.cooler_wrong_socket = {
            "socket_compatibility": ["AM4"],
            "tdp_rating": 150
        }
        self.cooler_low_tdp = {
            "socket_compatibility": ["LGA1700"],
            "tdp_rating": 100
        }
        self.cooler_no_sockets = {"tdp_rating": 150}
        
        # RAM specs
        self.ram_ddr4 = {
            "memory_type": "DDR4",
            "total_capacity_gb": 64
        }
        self.ram_ddr5 = {
            "memory_type": "DDR5",
            "total_capacity_gb": 64
        }
        
        # CPU with memory controller
        self.cpu_with_ddr4_controller = {
            "memory_controller": {
                "supported_types": ["DDR4"],
                "max_capacity": 128
            }
        }
        self.cpu_with_ddr5_controller = {
            "memory_controller": {
                "supported_types": ["DDR5"],
                "max_capacity": 128
            }
        }
        self.cpu_limited_capacity = {
            "memory_controller": {
                "supported_types": ["DDR4"],
                "max_capacity": 32
            }
        }
    
    # ----- Motherboard Tests -----
    
    def test_cpu_mobo_matching_sockets(self):
        """Test valid: CPU and motherboard have matching sockets."""
        result = check_cpu_with_component("motherboard", self.cpu_lga1700, self.mobo_lga1700)
        self.assertTrue(result)
    
    def test_cpu_mobo_different_sockets(self):
        """Test invalid: CPU and motherboard have different sockets."""
        result = check_cpu_with_component("motherboard", self.cpu_lga1700, self.mobo_am5)
        self.assertFalse(result)
    
    def test_cpu_mobo_missing_socket(self):
        """Test invalid: Motherboard missing socket specification."""
        result = check_cpu_with_component("motherboard", self.cpu_lga1700, self.mobo_no_socket)
        self.assertFalse(result)
    
    # ----- Cooler Tests -----
    
    def test_cpu_cooler_compatible_socket_and_tdp(self):
        """Test valid: Cooler supports CPU socket and has sufficient TDP."""
        result = check_cpu_with_component("cooler", self.cpu_lga1700, self.cooler_compatible)
        self.assertTrue(result)

    def test_cpu_cooler_no_socket_list(self):
        """Test valid: Cooler without socket list assumes compatibility."""
        result = check_cpu_with_component("cooler", self.cpu_lga1700, self.cooler_no_sockets)
        self.assertTrue(result)

    def test_cpu_cooler_incompatible_socket(self):
        """Test invalid: Cooler does not support CPU socket."""
        result = check_cpu_with_component("cooler", self.cpu_lga1700, self.cooler_wrong_socket)
        self.assertFalse(result)
    
    def test_cpu_cooler_insufficient_tdp(self):
        """Test invalid: Cooler TDP rating insufficient for CPU."""
        result = check_cpu_with_component("cooler", self.cpu_high_tdp, self.cooler_low_tdp)
        self.assertFalse(result)
      
    # ----- RAM Tests -----
    
    def test_cpu_ram_compatible_type_and_capacity(self):
        """Test valid: CPU supports RAM type and capacity."""
        result = check_cpu_with_component("ram", self.cpu_with_ddr4_controller, self.ram_ddr4)
        self.assertTrue(result)
    
    def test_cpu_ram_unsupported_type(self):
        """Test invalid: CPU does not support RAM type."""
        result = check_cpu_with_component("ram", self.cpu_with_ddr4_controller, self.ram_ddr5)
        self.assertFalse(result)
    
    def test_cpu_ram_exceeds_max_capacity(self):
        """Test invalid: RAM capacity exceeds CPU maximum."""
        result = check_cpu_with_component("ram", self.cpu_limited_capacity, self.ram_ddr4)
        self.assertFalse(result)

class TestCheckCaseWithComponent(unittest.TestCase):
    """
    Test cases for check_case_with_component function.

    Tests are organized by component type (motherboard, cooler, gpu, psu)

    Equivalence Partitions Tested - Motherboard:
        Valid:
            - Case supports motherboard form factor
        Invalid:
            - Case does not support motherboard form factor

    Equivalence Partitions Tested - Cooler:
        Valid:
            - Cooler height fits within case limit
        Invalid:
            - Cooler height exceeds case limit

    Equivalence Partitions Tested - GPU:
        Valid:
            - GPU length fits within case limit
        Invalid:
            - GPU length exceeds case limit

    Equivalence Partitions Tested - PSU:
        Valid:
            - Case supports PSU form factor
        Invalid:
            - Case does not support PSU form factor
    """
    
    def setUp(self):
        """Set up test data for case compatibility checks."""
        self.case_atx = {
            "supported_form_factors": ["ATX", "Micro-ATX"],
            "max_cpu_cooler_height": 165,
            "max_gpu_length": 350,
            "supported_psu_form_factors": ["ATX", "SFX"]
        }
        self.case_small = {
            "supported_form_factors": ["Mini-ITX"],
            "max_cpu_cooler_height": 80,
            "max_gpu_length": 200,
            "supported_psu_form_factors": ["SFX"]
        }
        
        # Motherboard specs
        self.mobo_atx = {"form_factor": "ATX"}
        self.mobo_eatx = {"form_factor": "E-ATX"}
        
        # Cooler specs
        self.cooler_short = {"height_mm": 150}
        self.cooler_tall = {"height_mm": 170}
        
        # GPU specs
        self.gpu_short = {"length_mm": 300}
        self.gpu_long = {"length_mm": 360}
        
        # PSU specs
        self.psu_atx = {"form_factor": "ATX"}
        self.psu_sfx = {"form_factor": "SFX"}
    
     # ----- Motherboard Tests -----
    def test_case_mobo_compatible_form_factor(self):
        """Test valid: Case supports motherboard form factor."""
        result = check_case_with_component("motherboard", self.case_atx, self.mobo_atx)
        self.assertTrue(result)
    
    def test_case_mobo_incompatible_form_factor(self):
        """Test invalid: Case does not support motherboard form factor."""
        result = check_case_with_component("motherboard", self.case_small, self.mobo_atx)
        self.assertFalse(result)
    
    # ----- Cooler Tests -----
    def test_case_cooler_fits_height(self):
        """Test valid: Cooler height fits within case limit."""
        result = check_case_with_component("cooler", self.case_atx, self.cooler_short)
        self.assertTrue(result)
    
    def test_case_cooler_too_tall(self):
        """Test invalid: Cooler height exceeds case limit."""
        result = check_case_with_component("cooler", self.case_small, self.cooler_short)
        self.assertFalse(result)
    
    # ----- GPU Tests -----
    def test_case_gpu_fits_length(self):
        """Test valid: GPU length fits within case limit."""
        result = check_case_with_component("gpu", self.case_atx, self.gpu_short)
        self.assertTrue(result)
    
    def test_case_gpu_too_long(self):
        """Test invalid: GPU length exceeds case limit."""
        result = check_case_with_component("gpu", self.case_small, self.gpu_short)
        self.assertFalse(result)
    
    # ----- PSU Tests -----
    def test_case_psu_compatible_form_factor(self):
        """Test valid: Case supports PSU form factor."""
        result = check_case_with_component("psu", self.case_atx, self.psu_atx)
        self.assertTrue(result)
    
    def test_case_psu_incompatible_form_factor(self):
        """Test invalid: Case does not support PSU form factor."""
        result = check_case_with_component("psu", self.case_small, self.psu_atx)
        self.assertFalse(result)

class TestCheckMotherboardWithComponent(unittest.TestCase):
    """
    Test cases for check_motherboard_with_component function.

    Tests are organized by component type (case, cpu, cooler)

    Equivalence Partitions Tested - Case:
        Valid:
            - Case supports motherboard form factor
        Invalid:
            - Case does not support motherboard form factor

    Equivalence Partitions Tested - CPU:
        Valid:
            - Motherboard socket matches CPU socket
        Invalid:
            - Motherboard socket does not match CPU socket

    Equivalence Partitions Tested - Cooler:
        Valid:
            - Cooler supports motherboard socket
        Invalid:
            - Cooler does not support motherboard socket
    """
    
    def setUp(self):
        """Set up test data for motherboard compatibility checks."""
        self.mobo_atx = {"form_factor": "ATX", "socket": "LGA1700"}
        self.mobo_am5 = {"form_factor": "Micro-ATX", "socket": "AM5"}
        
        self.case_atx = {"supported_form_factors": ["ATX", "Micro-ATX"]}
        self.case_mini = {"supported_form_factors": ["Mini-ITX"]}
        
        self.cpu_lga1700 = {"socket": "LGA1700"}
        self.cpu_am5 = {"socket": "AM5"}
        
        self.cooler_compatible = {"socket_compatibility": ["LGA1700", "AM5"]}
        self.cooler_incompatible = {"socket_compatibility": ["AM4"]}
    
    # ----- Case Tests -----
    def test_mobo_case_compatible(self):
        """Test valid: Case supports motherboard form factor."""
        result = check_motherboard_with_component("case", self.mobo_atx, self.case_atx)
        self.assertTrue(result)
    
    def test_mobo_case_incompatible(self):
        """Test invalid: Case does not support motherboard form factor."""
        result = check_motherboard_with_component("case", self.mobo_atx, self.case_mini)
        self.assertFalse(result)
    
    # ----- CPU Tests -----
    def test_mobo_cpu_matching_socket(self):
        """Test valid: Motherboard socket matches CPU socket."""
        result = check_motherboard_with_component("cpu", self.mobo_atx, self.cpu_lga1700)
        self.assertTrue(result)
    
    def test_mobo_cpu_different_socket(self):
        """Test invalid: Motherboard socket does not match CPU socket."""
        result = check_motherboard_with_component("cpu", self.mobo_atx, self.cpu_am5)
        self.assertFalse(result)
    
    # ----- Cooler Tests -----
    def test_mobo_cooler_compatible_socket(self):
        """Test valid: Cooler supports motherboard socket."""
        result = check_motherboard_with_component("cooler", self.mobo_atx, self.cooler_compatible)
        self.assertTrue(result)
    
    def test_mobo_cooler_incompatible_socket(self):
        """Test invalid: Cooler does not support motherboard socket."""
        result = check_motherboard_with_component("cooler", self.mobo_atx, self.cooler_incompatible)
        self.assertFalse(result)

class TestCheckCoolerWithComponent(unittest.TestCase):
    """
    Test cases for check_cooler_with_component function.

    Tests are organized by component type (case, motherboard, cpu)

    Equivalence Partitions Tested - Case:
        Valid:
            - Cooler height fits in case
        Invalid:
            - Cooler height exceeds case limit

    Equivalence Partitions Tested - Motherboard:
        Valid:
            - Cooler supports motherboard socket
        Invalid:
            - Cooler does not support motherboard socket

    Equivalence Partitions Tested - CPU:
        Valid:
            - Cooler supports CPU socket and has sufficient TDP
        Invalid:
            - Cooler does not support CPU socket
            - Cooler TDP insufficient for CPU
    """
    
    def setUp(self):
        """Set up test data for cooler compatibility checks."""
        self.cooler_short = {"height_mm": 150, "socket_compatibility": ["LGA1700"], "tdp_rating": 150}
        self.cooler_tall = {"height_mm": 180, "socket_compatibility": ["AM5"], "tdp_rating": 100}
        
        self.case_big = {"max_cpu_cooler_height": 165}
        self.case_small = {"max_cpu_cooler_height": 140}
        
        self.mobo_lga1700 = {"socket": "LGA1700"}
        self.mobo_am5 = {"socket": "AM5"}
        
        self.cpu_lga1700 = {"socket": "LGA1700", "tdp_rating": 125}
        self.cpu_high_tdp = {"socket": "LGA1700", "tdp_rating": 200}
    
    # ----- Case Tests -----
    def test_cooler_case_fits_height(self):
        """Test valid: Cooler height fits in case."""
        result = check_cooler_with_component("case", self.cooler_short, self.case_big)
        self.assertTrue(result)
    
    def test_cooler_case_too_tall(self):
        """Test invalid: Cooler height exceeds case limit."""
        result = check_cooler_with_component("case", self.cooler_tall, self.case_big)
        self.assertFalse(result)
    
    # ----- Motherboard Tests -----
    def test_cooler_mobo_compatible_socket(self):
        """Test valid: Cooler supports motherboard socket."""
        result = check_cooler_with_component("motherboard", self.cooler_short, self.mobo_lga1700)
        self.assertTrue(result)
    
    def test_cooler_mobo_incompatible_socket(self):
        """Test invalid: Cooler does not support motherboard socket."""
        result = check_cooler_with_component("motherboard", self.cooler_short, self.mobo_am5)
        self.assertFalse(result)
    
    # ----- CPU Tests -----
    def test_cooler_cpu_compatible_socket_and_tdp(self):
        """Test valid: Cooler supports CPU socket and has sufficient TDP."""
        result = check_cooler_with_component("cpu", self.cooler_short, self.cpu_lga1700)
        self.assertTrue(result)
    
    def test_cooler_cpu_insufficient_tdp(self):
        """Test invalid: Cooler TDP insufficient for CPU."""
        result = check_cooler_with_component("cpu", self.cooler_tall, self.cpu_lga1700)
        self.assertFalse(result)
    
    def test_cooler_cpu_incompatible_socket(self):
        """Test invalid: Cooler does not support CPU socket."""
        result = check_cooler_with_component("cpu", self.cooler_tall, self.cpu_lga1700)
        self.assertFalse(result)

class TestCheckGPUWithComponent(unittest.TestCase):
    """
    Test cases for check_gpu_with_component function.

    Tests are organized by component type (case)

    Equivalence Partitions Tested - Case:
        Valid:
            - GPU length fits in case
        Invalid:
            - GPU length exceeds case limit
    """
    
    def setUp(self):
        """Set up test data for GPU compatibility checks."""
        self.gpu_short = {"length_mm": 250}
        self.gpu_long = {"length_mm": 400}
        
        self.case_big = {"max_gpu_length": 350}
        self.case_small = {"max_gpu_length": 300}

    def test_gpu_case_fits_length(self):
        """Test valid: GPU length fits in case."""
        result = check_gpu_with_component("case", self.gpu_short, self.case_big)
        self.assertTrue(result)
    
    def test_gpu_case_too_long(self):
        """Test invalid: GPU length exceeds case limit."""
        result = check_gpu_with_component("case", self.gpu_long, self.case_big)
        self.assertFalse(result)

class TestCheckPSUWithComponent(unittest.TestCase):
    """
    Test cases for check_psu_with_component function.

    Tests are organized by component type (case)

    Equivalence Partitions Tested - Case:
        Valid:
            - Case supports PSU form factor
        Invalid:
            - Case does not support PSU form factor
    """
    
    def setUp(self):
        """Set up test data for PSU compatibility checks."""
        self.psu_atx = {"form_factor": "ATX"}
        self.psu_sfx = {"form_factor": "SFX"}
        
        self.case_atx = {"supported_psu_form_factors": ["ATX"]}
        self.case_sfx = {"supported_psu_form_factors": ["SFX", "ATX"]}
    
    def test_psu_case_compatible_form_factor(self):
        """Test valid: Case supports PSU form factor."""
        result = check_psu_with_component("case", self.psu_atx, self.case_atx)
        self.assertTrue(result)
    
    def test_psu_case_incompatible_form_factor(self):
        """Test invalid: Case does not support PSU form factor."""
        result = check_psu_with_component("case", self.psu_sfx, self.case_atx)
        self.assertFalse(result)

class TestCheckRAMWithComponent(unittest.TestCase):
    """
    Test cases for check_ram_with_component function.

    Tests are organized by component type (motherboard, cpu)

    Equivalence Partitions Tested - Motherboard:
        Valid:
            - RAM type matches motherboard
            - RAM speed within motherboard limit
            - RAM capacity within motherboard limit
            - Number of RAM modules fits in motherboard slots
        Invalid:
            - RAM type does not match motherboard
            - RAM speed exceeds motherboard limit
            - RAM capacity exceeds motherboard limit
            - More RAM modules than motherboard slots

    Equivalence Partitions Tested - CPU:
        Valid:
            - CPU supports RAM type
            - RAM capacity within CPU limit
            - RAM speed within CPU limit
        Invalid:
            - CPU does not support RAM type
            - RAM capacity exceeds CPU limit
            - RAM speed exceeds CPU limit
    """
    
    def setUp(self):
        """Set up test data for RAM compatibility checks."""
        # RAM specs
        self.ram_ddr4_16gb = {
            "memory_type": "DDR4",
            "speed": 3200,
            "total_capacity_gb": 16,
            "module_count": 2
        }
        self.ram_ddr4_64gb = {
            "memory_type": "DDR4",
            "speed": 3600,
            "total_capacity_gb": 64,
            "module_count": 4
        }
        self.ram_ddr5 = {
            "memory_type": "DDR5",
            "speed": 6000,
            "total_capacity_gb": 32,
            "module_count": 2
        }
        
        # Motherboard specs
        self.mobo_ddr4 = {
            "memory_type": "DDR4",
            "max_memory_speed": 3600,
            "max_memory_capacity": 128,
            "memory_slots": 4
        }
        self.mobo_ddr5 = {
            "memory_type": "DDR5",
            "max_memory_speed": 6400,
            "max_memory_capacity": 128,
            "memory_slots": 4
        }
        self.mobo_limited = {
            "memory_type": "DDR4",
            "max_memory_speed": 2666,
            "max_memory_capacity": 32,
            "memory_slots": 2
        }
        
        # CPU with memory controller
        self.cpu_ddr4 = {
            "memory_controller": {
                "supported_types": ["DDR4"],
                "max_capacity": 128,
                "max_speed": {"ddr4": 3200}
            }
        }
        self.cpu_ddr5 = {
            "memory_controller": {
                "supported_types": ["DDR5"],
                "max_capacity": 128,
                "max_speed": {"ddr5": 5600}
            }
        }
    
    # ----- Motherboard Tests -----
    def test_ram_mobo_compatible_type(self):
        """Test valid: RAM type matches motherboard."""
        result = check_ram_with_component("motherboard", self.ram_ddr4_16gb, self.mobo_ddr4)
        self.assertTrue(result)
    
    def test_ram_mobo_wrong_type(self):
        """Test invalid: RAM type does not match motherboard."""
        result = check_ram_with_component("motherboard", self.ram_ddr5, self.mobo_ddr4)
        self.assertFalse(result)
    
    def test_ram_mobo_speed_within_limit(self):
        """Test valid: RAM speed within motherboard limit."""
        result = check_ram_with_component("motherboard", self.ram_ddr4_16gb, self.mobo_ddr4)
        self.assertTrue(result)
    
    def test_ram_mobo_speed_exceeds_limit(self):
        """Test invalid: RAM speed exceeds motherboard limit."""
        result = check_ram_with_component("motherboard", self.ram_ddr4_64gb, self.mobo_limited)
        self.assertFalse(result)
    
    def test_ram_mobo_capacity_within_limit(self):
        """Test valid: RAM capacity within motherboard limit."""
        result = check_ram_with_component("motherboard", self.ram_ddr4_16gb, self.mobo_ddr4)
        self.assertTrue(result)
    
    def test_ram_mobo_capacity_exceeds_limit(self):
        """Test invalid: RAM capacity exceeds motherboard limit."""
        result = check_ram_with_component("motherboard", self.ram_ddr4_64gb, self.mobo_limited)
        self.assertFalse(result)
    
    def test_ram_mobo_modules_fit_in_slots(self):
        """Test valid: Number of RAM modules fits in motherboard slots."""
        result = check_ram_with_component("motherboard", self.ram_ddr4_16gb, self.mobo_ddr4)
        self.assertTrue(result)
    
    def test_ram_mobo_too_many_modules(self):
        """Test invalid: More RAM modules than motherboard slots."""
        ram_8_modules = {"memory_type": "DDR4", "speed": 3200, "total_capacity_gb": 64, "module_count": 8}
        result = check_ram_with_component("motherboard", ram_8_modules, self.mobo_limited)
        self.assertFalse(result)
    
    # ----- CPU Tests -----
    def test_ram_cpu_compatible_type(self):
        """Test valid: CPU supports RAM type."""
        result = check_ram_with_component("cpu", self.ram_ddr4_16gb, self.cpu_ddr4)
        self.assertTrue(result)
    
    def test_ram_cpu_wrong_type(self):
        """Test invalid: CPU does not support RAM type."""
        result = check_ram_with_component("cpu", self.ram_ddr5, self.cpu_ddr4)
        self.assertFalse(result)
    
    def test_ram_cpu_capacity_within_limit(self):
        """Test valid: RAM capacity within CPU limit."""
        result = check_ram_with_component("cpu", self.ram_ddr4_16gb, self.cpu_ddr4)
        self.assertTrue(result)
    
    def test_ram_cpu_speed_within_limit(self):
        """Test valid: RAM speed within CPU limit."""
        result = check_ram_with_component("cpu", self.ram_ddr4_16gb, self.cpu_ddr4)
        self.assertTrue(result)
    
    def test_ram_cpu_speed_exceeds_limit(self):
        """Test invalid: RAM speed exceeds CPU limit."""
        fast_ram = {"memory_type": "DDR4", "speed": 4000, "total_capacity_gb": 16, "module_count": 2}
        result = check_ram_with_component("cpu", fast_ram, self.cpu_ddr4)
        self.assertFalse(result)

class TestCalculateFunctions(unittest.TestCase):
    """
    Test cases for all calculate_*_compatibility functions.

    These functions test complete components against a selected build.

    Equivalence Partitions Tested:
        Valid:
            - Component fully compatible with all build components
            - GPU compatible when no case selected (edge case)
        Invalid:
            - CPU socket incompatible with motherboard
            - Case does not support motherboard form factor
            - Motherboard socket incompatible with CPU
            - Cooler too tall for case
            - GPU too long for case
            - PSU form factor not supported by case
            - RAM incompatible with motherboard
    """
    
    def setUp(self):
        """Set up test components and builds."""
        # Individual components
        self.cpu_intel = {
            "name": "Intel i7-12700K",
            "specs": {"socket": "LGA1700", "tdp_rating": 125}
        }
        self.cpu_amd = {
            "name": "AMD Ryzen 7",
            "specs": {"socket": "AM5", "tdp_rating": 105}
        }
        
        self.mobo_intel = {
            "name": "Z690 Aorus",
            "specs": {"form_factor": "ATX", "socket": "LGA1700", "memory_type": "DDR4", "max_memory_speed": 3600, "max_memory_capacity": 128, "memory_slots": 4
}
        }
        self.mobo_amd = {
            "name": "B650 Tomahawk",
            "specs": {"form_factor": "ATX", "socket": "AM5", "memory_type": "DDR5", "max_memory_speed": 6400, "max_memory_capacity": 128, "memory_slots": 4}
        }
        
        self.cooler = {
            "name": "Noctua NH-D15",
            "specs": {
                "height_mm": 165,
                "socket_compatibility": ["LGA1700", "AM5"],
                "tdp_rating": 150
            }
        }
        
        self.case = {
            "name": "Fractal Meshify C",
            "specs": {
                "supported_form_factors": ["ATX", "Micro-ATX"],
                "max_cpu_cooler_height": 170,
                "max_gpu_length": 350,
                "supported_psu_form_factors": ["ATX"]
            }
        }
        
        self.gpu = {
            "name": "RTX 3080",
            "specs": {"length_mm": 320}
        }
        
        self.psu = {
            "name": "Corsair RM750",
            "specs": {"form_factor": "ATX"}
        }
        
        self.ram = {
            "name": "Corsair Vengeance 32GB",
            "specs": {
                "memory_type": "DDR4",
                "speed": 3200,
                "total_capacity_gb": 32,
                "module_count": 2
            }
        }
        
        # Fully compatible build
        self.compatible_build = {
            "motherboard": self.mobo_intel,
            "cpu": self.cpu_intel,
            "cooler": self.cooler,
            "case": self.case,
            "gpu": self.gpu,
            "psu": self.psu,
            "ram": self.ram
        }
    
    # ----- calculate_cpu_compatibility Tests -----
    def test_cpu_compatible_with_build(self):
        """Test valid: CPU compatible with all build components."""
        result = calculate_cpu_compatibility(self.cpu_intel, self.compatible_build)
        self.assertTrue(result["compatible"])
        self.assertEqual(result["name"], "Intel i7-12700K")
        self.assertEqual(result["reasons"], [])
    
    def test_cpu_incompatible_socket_with_motherboard(self):
        """Test invalid: CPU socket incompatible with motherboard."""
        result = calculate_cpu_compatibility(self.cpu_amd, self.compatible_build)
        self.assertFalse(result["compatible"])
        self.assertIn("CPU socket does not match motherboard", result["reasons"])
    
    # ----- calculate_case_compatibility Tests -----   
    def test_case_compatible_with_build(self):
        """Test valid: Case compatible with all build components."""
        result = calculate_case_compatibility(self.case, self.compatible_build)
        self.assertTrue(result["compatible"])
        self.assertEqual(result["name"], "Fractal Meshify C")
    
    def test_case_incompatible_motherboard_form_factor(self):
        """Test invalid: Case doesn't support motherboard form factor."""
        small_case = {
            "name": "Mini Case",
            "specs": {
                "supported_form_factors": ["Mini-ITX"],
                "max_cpu_cooler_height": 170,
                "max_gpu_length": 350,
                "supported_psu_form_factors": ["ATX"]
            }
        }
        result = calculate_case_compatibility(small_case, self.compatible_build)
        self.assertFalse(result["compatible"])
        self.assertIn("Motherboard form factor not supported", result["reasons"])
    
    # ----- calculate_motherboard_compatibility Tests -----
    def test_motherboard_compatible_with_build(self):
        """Test valid: Motherboard compatible with all build components."""
        result = calculate_motherboard_compatibility(self.mobo_intel, self.compatible_build)
        self.assertTrue(result["compatible"])
    
    def test_motherboard_incompatible_cpu_socket(self):
        """Test invalid: Motherboard socket incompatible with CPU."""
        result = calculate_motherboard_compatibility(self.mobo_amd, self.compatible_build)
        self.assertFalse(result["compatible"])
        self.assertIn("CPU socket incompatible", result["reasons"])
    
    # ----- calculate_cooler_compatibility Tests -----
    def test_cooler_compatible_with_build(self):
        """Test valid: Cooler compatible with all build components."""
        result = calculate_cooler_compatibility(self.cooler, self.compatible_build)
        self.assertTrue(result["compatible"])
    
    def test_cooler_too_tall_for_case(self):
        """Test invalid: Cooler too tall for case."""
        tall_cooler = {
            "name": "Tall Cooler",
            "specs": {
                "height_mm": 200,
                "socket_compatibility": ["LGA1700"],
                "tdp_rating": 150
            }
        }
        result = calculate_cooler_compatibility(tall_cooler, self.compatible_build)
        self.assertFalse(result["compatible"])
        self.assertIn("Cooler too tall for case", result["reasons"])
    
    # ----- calculate_gpu_compatibility Tests -----
    def test_gpu_compatible_with_build(self):
        """Test valid: GPU compatible with case."""
        result = calculate_gpu_compatibility(self.gpu, self.compatible_build)
        self.assertTrue(result["compatible"])
    
    def test_gpu_too_long_for_case(self):
        """Test invalid: GPU too long for case."""
        long_gpu = {
            "name": "Long GPU",
            "specs": {"length_mm": 400}
        }
        result = calculate_gpu_compatibility(long_gpu, self.compatible_build)
        self.assertFalse(result["compatible"])
        self.assertIn("GPU too long for case", result["reasons"])
    
    def test_gpu_compatible_without_case(self):
        """Test valid: GPU considered compatible when no case selected."""
        build_without_case = {"cpu": self.cpu_intel}
        result = calculate_gpu_compatibility(self.gpu, build_without_case)
        self.assertTrue(result["compatible"])
        self.assertEqual(result["reasons"], [])
    
    # ----- calculate_psu_compatibility Tests -----
    def test_psu_compatible_with_build(self):
        """Test valid: PSU compatible with case."""
        result = calculate_psu_compatibility(self.psu, self.compatible_build)
        self.assertTrue(result["compatible"])
    
    def test_psu_incompatible_form_factor(self):
        """Test invalid: PSU form factor not supported by case."""
        sfx_psu = {
            "name": "SFX PSU",
            "specs": {"form_factor": "SFX"}
        }
        result = calculate_psu_compatibility(sfx_psu, self.compatible_build)
        self.assertFalse(result["compatible"])
        self.assertIn("PSU form factor not supported by case", result["reasons"])
    
    # ----- calculate_ram_compatibility Tests -----
    def test_ram_compatible_with_build(self):
        """Test valid: RAM compatible with motherboard and CPU."""
        result = calculate_ram_compatibility(self.ram, self.compatible_build)
        self.assertTrue(result["compatible"])
    
    def test_ram_incompatible_with_motherboard(self):
        """Test invalid: RAM incompatible with motherboard."""
        ddr5_ram = {
            "name": "DDR5 RAM",
            "specs": {
                "memory_type": "DDR5",
                "speed": 6000,
                "total_capacity_gb": 32,
                "module_count": 2
            }
        }
        result = calculate_ram_compatibility(ddr5_ram, self.compatible_build)
        self.assertFalse(result["compatible"])
        self.assertIn("RAM is not supported by motherboard", result["reasons"])

if __name__ == "__main__":
    unittest.main()