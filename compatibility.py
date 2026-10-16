# compatibility.py
"""
This module provides functions for checking compatibility between
PC components including CPU, motherboard, RAM, cooler, case, GPU, and PSU.
"""

def get_component_specs(component):
    """
    Safely extract specifications dictionary from a component.
    
    This function safely retrieves the 'specs' dictionary from a component
    object, returning an empty dictionary if the component is None or
    doesn't have specs.
    
    Characteristics:
        - Returns empty dict if component is None
        - Returns empty dict if 'specs' key doesn't exist
        - Returns component['specs'] otherwise
    
    Args:
        component (dict or None): Component dictionary containing specs
        
    Returns:
        dict: Component specifications dictionary, empty dict if not available
    
    Examples:
        >>> get_component_specs({"name": "CPU", "specs": {"socket": "LGA1700"}})
        {'socket': 'LGA1700'}
        >>> get_component_specs(None)
        {}
        >>> get_component_specs({"name": "No specs"})
        {}
    """
    if not component:
        return {}
    return component.get("specs", {})

def check_cpu_with_component(component_type, cpu_specs, other_specs):
    """
    Check if CPU is compatible with another component.
    
    This function validates CPU compatibility with motherboards (socket),
    coolers (socket + TDP), and RAM (memory controller specifications).
    
    Characteristics:
        - Motherboard: CPU socket must match motherboard socket
        - Cooler: CPU socket must be in cooler's compatibility list
        - Cooler: CPU TDP must not exceed cooler's TDP rating
        - RAM: RAM type must be supported by CPU memory controller
        - RAM: Total RAM capacity must not exceed CPU max capacity
    
    Args:
        component_type (str): Type of other component ('motherboard', 'cooler', or 'ram')
        cpu_specs (dict): CPU specifications dictionary
        other_specs (dict): Other component specifications dictionary
        
    Returns:
        bool: True if CPU is compatible, False otherwise
    
    Examples:
        >>> cpu = {"socket": "LGA1700", "tdp_rating": 125}
        >>> mobo = {"socket": "LGA1700"}
        >>> check_cpu_with_component("motherboard", cpu, mobo)
        True
        >>> check_cpu_with_component("motherboard", cpu, {"socket": "AM5"})
        False
    """
    
    if component_type == "motherboard":
        cpu_socket = cpu_specs.get("socket", "")
        mobo_socket = other_specs.get("socket", "")
        return cpu_socket == mobo_socket

    elif component_type == "cooler":
        cpu_socket = cpu_specs.get("socket", "")
        cooler_sockets = other_specs.get("socket_compatibility", [])
        
        if cooler_sockets and cpu_socket not in cooler_sockets:
            return False
        
        cpu_tdp = cpu_specs.get("tdp_rating", 0)
        cooler_tdp = other_specs.get("tdp_rating", 0)
        
        if cooler_tdp > 0 and cpu_tdp > cooler_tdp:
            return False
        
        return True

    elif component_type == "ram":
        memory_controller = cpu_specs.get("memory_controller", {})
        supported_types = memory_controller.get("supported_types", [])
        
        ram_type = other_specs.get("memory_type", "")
        if supported_types and ram_type not in supported_types:
            return False
        
        ram_capacity = other_specs.get("total_capacity_gb", 0)
        max_capacity = memory_controller.get("max_capacity", 999999)
        
        if ram_capacity > max_capacity:
            return False
        
        return True

    return True

def check_case_with_component(component_type, case_specs, other_specs):
    """
    Check if a case is compatible with another component.
    
    This function validates case compatibility with motherboards (form factor),
    coolers (height), GPUs (length), and PSUs (form factor).
    
    Characteristics:
        - Motherboard: Case must support motherboard form factor
        - Cooler: Cooler height must not exceed case max CPU cooler height
        - GPU: GPU length must not exceed case max GPU length
        - PSU: PSU form factor must be supported by case
    
    Args:
        component_type (str): Type of other component ('motherboard', 'cooler', 'gpu', or 'psu')
        case_specs (dict): Case specifications dictionary
        other_specs (dict): Other component specifications dictionary
        
    Returns:
        bool: True if case is compatible, False otherwise
    
    Examples:
        >>> case = {"supported_form_factors": ["ATX", "Micro-ATX"]}
        >>> mobo = {"form_factor": "ATX"}
        >>> check_case_with_component("motherboard", case, mobo)
        True
        >>> check_case_with_component("motherboard", case, {"form_factor": "E-ATX"})
        False
    """
    if component_type == "motherboard":
        form_factor = other_specs.get("form_factor", "")
        supported = case_specs.get("supported_form_factors", [])
        return form_factor in supported
    
    elif component_type == "cooler":
        cooler_height = other_specs.get("height_mm", 0)
        max_height = case_specs.get("max_cpu_cooler_height", 999999)
        return cooler_height <= max_height
    
    elif component_type == "gpu":
        gpu_length = other_specs.get("length_mm", 0)
        max_length = case_specs.get("max_gpu_length", 999999)
        return gpu_length <= max_length
    
    elif component_type == "psu":
        psu_form = other_specs.get("form_factor", "ATX")
        supported = case_specs.get("supported_psu_form_factors", ["ATX"])
        return psu_form in supported
    
    return True

def check_motherboard_with_component(component_type, mobo_specs, other_specs):
    """
    Check if a motherboard is compatible with another component.
    
    This function validates motherboard compatibility with cases (form factor),
    CPUs (socket), and coolers (socket compatibility).
    
    Characteristics:
        - Case: Motherboard form factor must be supported by case
        - CPU: Motherboard socket must match CPU socket
        - Cooler: Motherboard socket must be in cooler's compatibility list
    
    Args:
        component_type (str): Type of other component ('case', 'cpu', or 'cooler')
        mobo_specs (dict): Motherboard specifications dictionary
        other_specs (dict): Other component specifications dictionary
        
    Returns:
        bool: True if motherboard is compatible, False otherwise
    
    Examples:
        >>> mobo = {"form_factor": "ATX", "socket": "LGA1700"}
        >>> cpu = {"socket": "LGA1700"}
        >>> check_motherboard_with_component("cpu", mobo, cpu)
        True
    """
    if component_type == "case":
        mobo_form = mobo_specs.get("form_factor", "")
        case_supported = other_specs.get("supported_form_factors", [])
        return mobo_form in case_supported
    
    elif component_type == "cpu":
        cpu_socket = other_specs.get("socket", "")
        mobo_socket = mobo_specs.get("socket", "")
        return cpu_socket == mobo_socket
    
    elif component_type == "cooler":
        cooler_sockets = other_specs.get("socket_compatibility", [])
        mobo_socket = mobo_specs.get("socket", "")
        return mobo_socket in cooler_sockets
    
    return True

def check_cooler_with_component(component_type, cooler_specs, other_specs):
    """
    Check if a cooler is compatible with another component.
    
    This function validates cooler compatibility with cases (height),
    motherboards (socket), and CPUs (socket + TDP).
    
    Characteristics:
        - Case: Cooler height must not exceed case max CPU cooler height
        - Motherboard: Cooler socket list must include motherboard socket
        - CPU: Cooler socket list must include CPU socket
        - CPU: Cooler TDP rating must be sufficient for CPU TDP
    
    Args:
        component_type (str): Type of other component ('case', 'motherboard', or 'cpu')
        cooler_specs (dict): Cooler specifications dictionary
        other_specs (dict): Other component specifications dictionary
        
    Returns:
        bool: True if cooler is compatible, False otherwise
    """
    if component_type == "case":
        cooler_height = cooler_specs.get("height_mm", 0)
        max_height = other_specs.get("max_cpu_cooler_height", 999999)
        return cooler_height <= max_height
    
    elif component_type == "motherboard":
        cooler_sockets = cooler_specs.get("socket_compatibility", [])
        mobo_socket = other_specs.get("socket", "")
        return mobo_socket in cooler_sockets
    
    elif component_type == "cpu":
        cpu_socket = other_specs.get("socket", "")
        cooler_sockets = cooler_specs.get("socket_compatibility", [])
        if cpu_socket not in cooler_sockets:
            return False
        
        cpu_tdp = other_specs.get("tdp_rating", 0)
        cooler_tdp = cooler_specs.get("tdp_rating", 0)
        if cooler_tdp > 0 and cpu_tdp > cooler_tdp:
            return False
        
        return True
    
    return True

def check_gpu_with_component(component_type, gpu_specs, other_specs):
    """
    Check if a GPU is compatible with another component.
    
    This function validates GPU compatibility with cases (length).
    
    Characteristics:
        - Case: GPU length must not exceed case max GPU length
    
    Args:
        component_type (str): Type of other component ('case')
        gpu_specs (dict): GPU specifications dictionary
        other_specs (dict): Other component specifications dictionary
        
    Returns:
        bool: True if GPU is compatible, False otherwise
    """
    if component_type == "case":
        gpu_length = gpu_specs.get("length_mm", 0)
        max_length = other_specs.get("max_gpu_length", 999999)
        return gpu_length <= max_length
    
    return True

def check_psu_with_component(component_type, psu_specs, other_specs):
    """
    Check if a PSU is compatible with another component.
    
    This function validates PSU compatibility with cases (form factor).
    
    Characteristics:
        - Case: PSU form factor must be supported by case
    
    Args:
        component_type (str): Type of other component ('case')
        psu_specs (dict): PSU specifications dictionary
        other_specs (dict): Other component specifications dictionary
        
    Returns:
        bool: True if PSU is compatible, False otherwise
    """
    if component_type == "case":
        psu_form = psu_specs.get("form_factor", "ATX")
        case_supported = other_specs.get("supported_psu_form_factors", ["ATX"])
        return psu_form in case_supported
    
    return True

def check_ram_with_component(component_type, ram_specs, other_specs):
    """
    Check if RAM is compatible with another component.
    
    This function validates RAM compatibility with motherboards (type, speed,
    capacity, slots) and CPUs (memory controller).
    
    Characteristics:
        - Motherboard: RAM type must match motherboard
        - Motherboard: RAM speed must not exceed motherboard max speed
        - Motherboard: RAM capacity must not exceed motherboard max capacity
        - Motherboard: Number of modules must not exceed available slots
        - CPU: RAM type must be supported by CPU memory controller
        - CPU: RAM capacity must not exceed CPU max capacity
        - CPU: RAM speed must not exceed CPU max speed for that RAM type
    
    Args:
        component_type (str): Type of other component ('motherboard' or 'cpu')
        ram_specs (dict): RAM specifications dictionary
        other_specs (dict): Other component specifications dictionary
        
    Returns:
        bool: True if RAM is compatible, False otherwise
    """
    if component_type == "motherboard":
        ram_type = ram_specs.get("memory_type", "")
        mobo_type = other_specs.get("memory_type", "")
        if ram_type and mobo_type and ram_type != mobo_type:
            return False

        ram_speed = ram_specs.get("speed", 0)
        max_speed = other_specs.get("max_memory_speed", 999999)
        if ram_speed > max_speed:
            return False

        ram_capacity = ram_specs.get("total_capacity_gb", 0)
        max_capacity = other_specs.get("max_memory_capacity", 999999)
        if ram_capacity > max_capacity:
            return False

        ram_modules = ram_specs.get("module_count", 0)
        memory_slots = other_specs.get("memory_slots", 999999)
        if ram_modules > memory_slots:
            return False

        return True

    elif component_type == "cpu":
        memory_controller = other_specs.get("memory_controller", {})
        supported_types = memory_controller.get("supported_types", [])
        ram_type = ram_specs.get("memory_type", "")

        if supported_types and ram_type not in supported_types:
            return False

        max_capacity = memory_controller.get("max_capacity", 999999)
        ram_capacity = ram_specs.get("total_capacity_gb", 0)
        if ram_capacity > max_capacity:
            return False

        max_speed_data = memory_controller.get("max_speed", {})
        ram_speed = ram_specs.get("speed", 0)

        if isinstance(max_speed_data, dict):
            ram_type_key = ram_type.lower()
            cpu_max_speed = max_speed_data.get(ram_type_key, 999999)
            if ram_speed > cpu_max_speed:
                return False

        return True

    return True

def calculate_cpu_compatibility(cpu, selected_build):
    """
    Calculate compatibility for a CPU against the selected build.
    
    This function checks a candidate CPU against all components in the
    selected build (motherboard, cooler, RAM) and returns a compatibility report.
    
    Characteristics:
        - Checks socket compatibility with motherboard
        - Checks socket and TDP compatibility with cooler
        - Checks memory controller compatibility with RAM
    
    Args:
        cpu (dict): CPU component dictionary with 'name' and 'specs' keys
        selected_build (dict): Dictionary of selected components
        
    Returns:
        dict: Dictionary with keys:
            - 'name': CPU name
            - 'compatible': Boolean indicating overall compatibility
            - 'reasons': List of incompatibility reasons (empty if compatible)
    
    Examples:
        >>> cpu = {"name": "Intel i7", "specs": {"socket": "LGA1700"}}
        >>> build = {"motherboard": {"specs": {"socket": "LGA1700"}}}
        >>> calculate_cpu_compatibility(cpu, build)
        {'name': 'Intel i7', 'compatible': True, 'reasons': []}
    """
    compatible = True
    reasons = []
    cpu_specs = get_component_specs(cpu)

    if selected_build.get("motherboard"):
        if not check_cpu_with_component("motherboard", cpu_specs, get_component_specs(selected_build["motherboard"])):
            compatible = False
            reasons.append("CPU socket does not match motherboard")

    if selected_build.get("cooler"):
        if not check_cpu_with_component("cooler", cpu_specs, get_component_specs(selected_build["cooler"])):
            compatible = False
            reasons.append("CPU is not supported by cooler")

    if selected_build.get("ram"):
        if not check_cpu_with_component("ram", cpu_specs, get_component_specs(selected_build["ram"])):
            compatible = False
            reasons.append("CPU does not support selected RAM")

    return {
        "name": cpu["name"],
        "compatible": compatible,
        "reasons": reasons if not compatible else []
    }

def calculate_case_compatibility(case, selected_build):
    """
    Calculate compatibility for a case against the selected build.
    
    This function checks a candidate case against all components in the
    selected build (motherboard, cooler, GPU, PSU) and returns a compatibility report.
    
    Characteristics:
        - Checks form factor compatibility with motherboard
        - Checks CPU cooler height clearance
        - Checks GPU length clearance
        - Checks PSU form factor support
    
    Args:
        case (dict): Case component dictionary with 'name' and 'specs' keys
        selected_build (dict): Dictionary of selected components
        
    Returns:
        dict: Dictionary with keys:
            - 'name': Case name
            - 'compatible': Boolean indicating overall compatibility
            - 'reasons': List of incompatibility reasons (empty if compatible)
    """
    compatible = True
    reasons = []
    case_specs = get_component_specs(case)
    
    if selected_build.get("motherboard"):
        if not check_case_with_component("motherboard", case_specs, get_component_specs(selected_build["motherboard"])):
            compatible = False
            reasons.append("Motherboard form factor not supported")
    
    if selected_build.get("cooler"):
        if not check_case_with_component("cooler", case_specs, get_component_specs(selected_build["cooler"])):
            compatible = False
            reasons.append("CPU cooler height too tall")
    
    if selected_build.get("gpu"):
        if not check_case_with_component("gpu", case_specs, get_component_specs(selected_build["gpu"])):
            compatible = False
            reasons.append("GPU too long for case")
    
    if selected_build.get("psu"):
        if not check_case_with_component("psu", case_specs, get_component_specs(selected_build["psu"])):
            compatible = False
            reasons.append("PSU form factor not supported")
    
    return {
        "name": case["name"],
        "compatible": compatible,
        "reasons": reasons if not compatible else []
    }

def calculate_motherboard_compatibility(motherboard, selected_build):
    """
    Calculate compatibility for a motherboard against the selected build.
    
    This function checks a candidate motherboard against all components in the
    selected build (case, CPU, cooler) and returns a compatibility report.
    
    Characteristics:
        - Checks form factor compatibility with case
        - Checks socket compatibility with CPU
        - Checks socket compatibility with cooler
    
    Args:
        motherboard (dict): Motherboard component dictionary with 'name' and 'specs' keys
        selected_build (dict): Dictionary of selected components
        
    Returns:
        dict: Dictionary with keys:
            - 'name': Motherboard name
            - 'compatible': Boolean indicating overall compatibility
            - 'reasons': List of incompatibility reasons (empty if compatible)
    """
    compatible = True
    reasons = []
    mobo_specs = get_component_specs(motherboard)
    
    if selected_build.get("case"):
        if not check_motherboard_with_component("case", mobo_specs, get_component_specs(selected_build["case"])):
            compatible = False
            reasons.append("Case does not support this motherboard form factor")
    
    if selected_build.get("cpu"):
        if not check_motherboard_with_component("cpu", mobo_specs, get_component_specs(selected_build["cpu"])):
            compatible = False
            reasons.append("CPU socket incompatible")
    
    if selected_build.get("cooler"):
        if not check_motherboard_with_component("cooler", mobo_specs, get_component_specs(selected_build["cooler"])):
            compatible = False
            reasons.append("Cooler does not support this motherboard socket")
    
    return {
        "name": motherboard["name"],
        "compatible": compatible,
        "reasons": reasons if not compatible else []
    }

def calculate_cooler_compatibility(cooler, selected_build):
    """
    Calculate compatibility for a cooler against the selected build.
    
    This function checks a candidate cooler against all components in the
    selected build (case, motherboard, CPU) and returns a compatibility report.
    
    Characteristics:
        - Checks height clearance with case
        - Checks socket compatibility with motherboard
        - Checks socket and TDP compatibility with CPU
    
    Args:
        cooler (dict): Cooler component dictionary with 'name' and 'specs' keys
        selected_build (dict): Dictionary of selected components
        
    Returns:
        dict: Dictionary with keys:
            - 'name': Cooler name
            - 'compatible': Boolean indicating overall compatibility
            - 'reasons': List of incompatibility reasons (empty if compatible)
    """
    compatible = True
    reasons = []
    cooler_specs = get_component_specs(cooler)
    
    if selected_build.get("case"):
        if not check_cooler_with_component("case", cooler_specs, get_component_specs(selected_build["case"])):
            compatible = False
            reasons.append("Cooler too tall for case")
    
    if selected_build.get("motherboard"):
        if not check_cooler_with_component("motherboard", cooler_specs, get_component_specs(selected_build["motherboard"])):
            compatible = False
            reasons.append("Cooler does not support motherboard socket")
    
    if selected_build.get("cpu"):
        if not check_cooler_with_component("cpu", cooler_specs, get_component_specs(selected_build["cpu"])):
            compatible = False
            reasons.append("Cooler does not support CPU socket or insufficient TDP")
    
    return {
        "name": cooler["name"],
        "compatible": compatible,
        "reasons": reasons if not compatible else []
    }

def calculate_gpu_compatibility(gpu, selected_build):
    """
    Calculate compatibility for a GPU against the selected build.
    
    This function checks a candidate GPU against all components in the
    selected build (case) and returns a compatibility report.
    
    Characteristics:
        - Checks length clearance with case
    
    Args:
        gpu (dict): GPU component dictionary with 'name' and 'specs' keys
        selected_build (dict): Dictionary of selected components
        
    Returns:
        dict: Dictionary with keys:
            - 'name': GPU name
            - 'compatible': Boolean indicating overall compatibility
            - 'reasons': List of incompatibility reasons (empty if compatible)
    """
    compatible = True
    reasons = []
    gpu_specs = get_component_specs(gpu)
    
    if selected_build.get("case"):
        if not check_gpu_with_component("case", gpu_specs, get_component_specs(selected_build["case"])):
            compatible = False
            reasons.append("GPU too long for case")
    
    return {
        "name": gpu["name"],
        "compatible": compatible,
        "reasons": reasons if not compatible else []
    }

def calculate_psu_compatibility(psu, selected_build):
    """
    Calculate compatibility for a PSU against the selected build.
    
    This function checks a candidate PSU against all components in the
    selected build (case) and returns a compatibility report.
    
    Characteristics:
        - Checks form factor support with case
    
    Args:
        psu (dict): PSU component dictionary with 'name' and 'specs' keys
        selected_build (dict): Dictionary of selected components
        
    Returns:
        dict: Dictionary with keys:
            - 'name': PSU name
            - 'compatible': Boolean indicating overall compatibility
            - 'reasons': List of incompatibility reasons (empty if compatible)
    """
    compatible = True
    reasons = []
    psu_specs = get_component_specs(psu)
    
    if selected_build.get("case"):
        if not check_psu_with_component("case", psu_specs, get_component_specs(selected_build["case"])):
            compatible = False
            reasons.append("PSU form factor not supported by case")
    
    return {
        "name": psu["name"],
        "compatible": compatible,
        "reasons": reasons if not compatible else []
    }

def calculate_ram_compatibility(ram, selected_build):
    """
    Calculate compatibility for a RAM kit against the selected build.
    
    This function checks a candidate RAM kit against all components in the
    selected build (motherboard, CPU) and returns a compatibility report.
    
    Characteristics:
        - Checks type, speed, capacity, and slot count with motherboard
        - Checks memory controller compatibility with CPU
    
    Args:
        ram (dict): RAM component dictionary with 'name' and 'specs' keys
        selected_build (dict): Dictionary of selected components
        
    Returns:
        dict: Dictionary with keys:
            - 'name': RAM name
            - 'compatible': Boolean indicating overall compatibility
            - 'reasons': List of incompatibility reasons (empty if compatible)
    """
    compatible = True
    reasons = []
    ram_specs = get_component_specs(ram)

    if selected_build.get("motherboard"):
        if not check_ram_with_component("motherboard", ram_specs, get_component_specs(selected_build["motherboard"])):
            compatible = False
            reasons.append("RAM is not supported by motherboard")

    if selected_build.get("cpu"):
        if not check_ram_with_component("cpu", ram_specs, get_component_specs(selected_build["cpu"])):
            compatible = False
            reasons.append("RAM is not supported by CPU memory controller")

    return {
        "name": ram["name"],
        "compatible": compatible,
        "reasons": reasons if not compatible else []
    }