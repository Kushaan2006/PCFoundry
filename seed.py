"""Seed data for PCFoundry products."""

from db import db

products_col = db["products"]
reviews_col = db["reviews"]

products = [
  {
    "name": "NZXT H5 Flow",
    "brand": "NZXT",
    "type": "case",
    "price": 129.99,
    "stock": 12,
    "ratings": [5, 4, 4, 5, 3, 4, 5, 4],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 365,
      "max_cpu_cooler_height": 165,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Lian Li O11 Dynamic EVO",
    "brand": "Lian Li",
    "type": "case",
    "price": 199.99,
    "stock": 8,
    "ratings": [5, 4, 5, 4, 4, 5, 5],
    "specs": {
      "supported_form_factors": ["E-ATX", "ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 422,
      "max_cpu_cooler_height": 167,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Fractal Design Pop Air",
    "brand": "Fractal",
    "type": "case",
    "price": 109.99,
    "stock": 20,
    "ratings": [4, 4, 3, 4, 5, 4],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 405,
      "max_cpu_cooler_height": 170,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Corsair 4000D Airflow",
    "brand": "Corsair",
    "type": "case",
    "price": 119.99,
    "stock": 25,
    "ratings": [5, 4, 5, 4, 4, 5, 3, 4, 5],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 360,
      "max_cpu_cooler_height": 170,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Cooler Master NR200P",
    "brand": "Cooler Master",
    "type": "case",
    "price": 129.99,
    "stock": 15,
    "ratings": [5, 4, 4, 5, 3],
    "specs": {
      "supported_form_factors": ["Mini-ITX"],
      "max_gpu_length": 330,
      "max_cpu_cooler_height": 155,
      "supported_psu_form_factors": ["SFX", "SFX-L"]
    }
  },
  {
    "name": "Fractal Design North",
    "brand": "Fractal",
    "type": "case",
    "price": 159.99,
    "stock": 10,
    "ratings": [],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 355,
      "max_cpu_cooler_height": 170,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Montech AIR 903 Max",
    "brand": "Montech",
    "type": "case",
    "price": 89.99,
    "stock": 30,
    "ratings": [4, 4, 4, 5, 4, 3],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 400,
      "max_cpu_cooler_height": 180,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "HYTE Y60",
    "brand": "HYTE",
    "type": "case",
    "price": 199.99,
    "stock": 8,
    "ratings": [5, 4, 4, 5, 3, 4],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 375,
      "max_cpu_cooler_height": 160,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Deepcool CH560",
    "brand": "Deepcool",
    "type": "case",
    "price": 109.99,
    "stock": 18,
    "ratings": [4, 4, 4, 5, 3, 4, 4],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 380,
      "max_cpu_cooler_height": 175,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Phanteks Eclipse G360A",
    "brand": "Phanteks",
    "type": "case",
    "price": 99.99,
    "stock": 22,
    "ratings": [4, 5, 4, 4, 3, 4, 5, 4],
    "specs": {
      "supported_form_factors": ["ATX", "Micro-ATX", "Mini-ITX"],
      "max_gpu_length": 400,
      "max_cpu_cooler_height": 162,
      "supported_psu_form_factors": ["ATX"]
    }
  },
  {
    "name": "Deepcool AK620",
    "brand": "Deepcool",
    "type": "cooler",
    "price": 79.99,
    "stock": 18,
    "ratings": [5, 4, 5, 4, 4, 3, 5, 4, 4],
    "specs": {
      "cooler_type": "air",
      "socket_compatibility": ["LGA1700", "LGA1200", "AM5", "AM4"],
      "tdp_rating": 260,
      "height_mm": 160
    }
  },
  {
    "name": "Noctua NH-D15",
    "brand": "Noctua",
    "type": "cooler",
    "price": 119.99,
    "stock": 12,
    "ratings": [5, 5, 4, 5, 5, 4, 5, 4],
    "specs": {
      "cooler_type": "air",
      "socket_compatibility": ["LGA1700", "LGA1200", "LGA115X", "AM5", "AM4"],
      "tdp_rating": 250,
      "height_mm": 165
    }
  },
  {
    "name": "Cooler Master Hyper 212 Black",
    "brand": "Cooler Master",
    "type": "cooler",
    "price": 54.99,
    "stock": 35,
    "ratings": [4, 4, 3, 4, 5, 3, 4, 4, 2, 4],
    "specs": {
      "cooler_type": "air",
      "socket_compatibility": ["LGA1700", "LGA1200", "LGA115X", "AM5", "AM4"],
      "tdp_rating": 150,
      "height_mm": 159
    }
  },
  {
    "name": "NZXT Kraken 360 RGB",
    "brand": "NZXT",
    "type": "cooler",
    "price": 229.99,
    "stock": 10,
    "ratings": [5, 4, 4, 5, 3, 4, 5],
    "specs": {
      "cooler_type": "aio",
      "socket_compatibility": ["LGA1700", "LGA1200", "AM5", "AM4"],
      "tdp_rating": 300,
      "radiator_size": 360
    }
  },
  {
    "name": "Corsair iCUE H100i Elite",
    "brand": "Corsair",
    "type": "cooler",
    "price": 159.99,
    "stock": 15,
    "ratings": [4, 4, 5, 4, 3, 4],
    "specs": {
      "cooler_type": "aio",
      "socket_compatibility": ["LGA1700", "LGA1200", "AM5", "AM4"],
      "tdp_rating": 250,
      "radiator_size": 240
    }
  },
  {
    "name": "Thermalright Peerless Assassin 120 SE",
    "brand": "Thermalright",
    "type": "cooler",
    "price": 49.99,
    "stock": 40,
    "ratings": [5, 5, 4, 5, 4, 4, 5, 5, 4, 5],
    "specs": {
      "cooler_type": "air",
      "socket_compatibility": ["LGA1700", "LGA1200", "LGA115X", "AM5", "AM4"],
      "tdp_rating": 265,
      "height_mm": 155
    }
  },
  {
    "name": "Arctic Liquid Freezer III 360",
    "brand": "Arctic",
    "type": "cooler",
    "price": 149.99,
    "stock": 12,
    "ratings": [5, 4, 5, 5, 4, 4, 5, 3],
    "specs": {
      "cooler_type": "aio",
      "socket_compatibility": ["LGA1700", "LGA1200", "AM5", "AM4"],
      "tdp_rating": 320,
      "radiator_size": 360
    }
  },
  {
    "name": "be quiet! Dark Rock Pro 5",
    "brand": "be quiet!",
    "type": "cooler",
    "price": 109.99,
    "stock": 14,
    "ratings": [5, 4, 5, 4, 4, 5, 4],
    "specs": {
      "cooler_type": "air",
      "socket_compatibility": ["LGA1700", "LGA1200", "LGA115X", "AM5", "AM4"],
      "tdp_rating": 270,
      "height_mm": 166
    }
  },
  {
    "name": "Lian Li Galahad II Trinity 240",
    "brand": "Lian Li",
    "type": "cooler",
    "price": 139.99,
    "stock": 18,
    "ratings": [4, 4, 5, 4, 3, 4, 4],
    "specs": {
      "cooler_type": "aio",
      "socket_compatibility": ["LGA1700", "LGA1200", "AM5", "AM4"],
      "tdp_rating": 280,
      "radiator_size": 240
    }
  },
  {
    "name": "ID-COOLING SE-214-XT",
    "brand": "ID-COOLING",
    "type": "cooler",
    "price": 24.99,
    "stock": 50,
    "ratings": [4, 3, 4, 4, 2, 3, 4, 5],
    "specs": {
      "cooler_type": "air",
      "socket_compatibility": ["LGA1700", "LGA1200", "LGA115X", "AM5", "AM4"],
      "tdp_rating": 180,
      "height_mm": 150
    }
  },
  {
    "name": "Intel Core i5-13600K",
    "brand": "Intel",
    "type": "cpu",
    "price": 409.99,
    "stock": 15,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "tdp_rating": 125,
      "integrated_graphics": True,
      "memory_controller": {
        "max_speed": {
          "ddr4": 3200,
          "ddr5": 5600
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR4", "DDR5"]
      }
    }
  },
  {
    "name": "Intel Core i7-13700K",
    "brand": "Intel",
    "type": "cpu",
    "price": 499.99,
    "stock": 12,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "tdp_rating": 125,
      "integrated_graphics": True,
      "memory_controller": {
        "max_speed": {
          "ddr4": 3200,
          "ddr5": 5600
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR4", "DDR5"]
      }
    }
  },
  {
    "name": "Intel Core i9-13900K",
    "brand": "Intel",
    "type": "cpu",
    "price": 729.99,
    "stock": 8,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "tdp_rating": 125,
      "integrated_graphics": True,
      "memory_controller": {
        "max_speed": {
          "ddr4": 3200,
          "ddr5": 5600
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR4", "DDR5"]
      }
    }
  },
  {
    "name": "Intel Core i3-13100F",
    "brand": "Intel",
    "type": "cpu",
    "price": 149.99,
    "stock": 30,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "tdp_rating": 60,
      "integrated_graphics": False,
      "memory_controller": {
        "max_speed": {
          "ddr4": 3200,
          "ddr5": 4800
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR4", "DDR5"]
      }
    }
  },
  {
    "name": "AMD Ryzen 5 7600X",
    "brand": "AMD",
    "type": "cpu",
    "price": 319.99,
    "stock": 22,
    "ratings": [],
    "specs": {
      "socket": "AM5",
      "tdp_rating": 105,
      "integrated_graphics": True,
      "memory_controller": {
        "max_speed": {
          "ddr5": 5200
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR5"]
      }
    }
  },
  {
    "name": "AMD Ryzen 7 7700X",
    "brand": "AMD",
    "type": "cpu",
    "price": 449.99,
    "stock": 18,
    "ratings": [],
    "specs": {
      "socket": "AM5",
      "tdp_rating": 105,
      "integrated_graphics": True,
      "memory_controller": {
        "max_speed": {
          "ddr5": 5200
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR5"]
      }
    }
  },
  {
    "name": "AMD Ryzen 7 7800X3D",
    "brand": "AMD",
    "type": "cpu",
    "price": 589.99,
    "stock": 10,
    "ratings": [],
    "specs": {
      "socket": "AM5",
      "tdp_rating": 120,
      "integrated_graphics": True,
      "memory_controller": {
        "max_speed": {
          "ddr5": 5200
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR5"]
      }
    }
  },
  {
    "name": "AMD Ryzen 5 5600X",
    "brand": "AMD",
    "type": "cpu",
    "price": 199.99,
    "stock": 25,
    "ratings": [],
    "specs": {
      "socket": "AM4",
      "tdp_rating": 65,
      "integrated_graphics": False,
      "memory_controller": {
        "max_speed": {
          "ddr4": 3200
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR4"]
      }
    }
  },
  {
    "name": "Intel Core i5-12400F",
    "brand": "Intel",
    "type": "cpu",
    "price": 189.99,
    "stock": 28,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "tdp_rating": 65,
      "integrated_graphics": False,
      "memory_controller": {
        "max_speed": {
          "ddr4": 3200,
          "ddr5": 4800
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR4", "DDR5"]
      }
    }
  },
  {
    "name": "AMD Ryzen 9 7950X",
    "brand": "AMD",
    "type": "cpu",
    "price": 849.99,
    "stock": 5,
    "ratings": [],
    "specs": {
      "socket": "AM5",
      "tdp_rating": 170,
      "integrated_graphics": True,
      "memory_controller": {
        "max_speed": {
          "ddr5": 5200
        },
        "max_capacity": 128,
        "channels": 2,
        "supported_types": ["DDR5"]
      }
    }
  },
  {
    "name": "XFX Speedster QICK 319 Radeon RX 7800 XT",
    "brand": "XFX",
    "type": "gpu",
    "price": 699.99,
    "stock": 8,
    "ratings": [],
    "specs": {
      "tdp_rating": 263,
      "length_mm": 335,
      "slot_width": 2.5,
      "required_pcie_version": "4.0",
      "power_connectors": "8-pin",
      "power_connector_count": 2,
      "vram_gb": 16,
      "vram_type": "GDDR6"
    }
  },
  {
    "name": "MSI GeForce RTX 4060 Ventus 2X",
    "brand": "MSI",
    "type": "gpu",
    "price": 399.99,
    "stock": 20,
    "ratings": [],
    "specs": {
      "tdp_rating": 115,
      "length_mm": 199,
      "slot_width": 2,
      "required_pcie_version": "4.0",
      "power_connectors": "8-pin",
      "power_connector_count": 1,
      "vram_gb": 8,
      "vram_type": "GDDR6"
    }
  },
  {
    "name": "ASUS TUF Gaming RTX 4070 Ti",
    "brand": "ASUS",
    "type": "gpu",
    "price": 1049.99,
    "stock": 5,
    "ratings": [],
    "specs": {
      "tdp_rating": 285,
      "length_mm": 305,
      "slot_width": 3.25,
      "required_pcie_version": "4.0",
      "power_connectors": "16-pin",
      "power_connector_count": 1,
      "vram_gb": 12,
      "vram_type": "GDDR6X"
    }
  },
  {
    "name": "Sapphire Pulse Radeon RX 6700 XT",
    "brand": "Sapphire",
    "type": "gpu",
    "price": 449.99,
    "stock": 12,
    "ratings": [],
    "specs": {
      "tdp_rating": 230,
      "length_mm": 280,
      "slot_width": 2.5,
      "required_pcie_version": "4.0",
      "power_connectors": "8-pin",
      "power_connector_count": 2,
      "vram_gb": 12,
      "vram_type": "GDDR6"
    }
  },
  {
    "name": "Gigabyte GeForce RTX 4090 Gaming OC",
    "brand": "Gigabyte",
    "type": "gpu",
    "price": 2499.99,
    "stock": 3,
    "ratings": [],
    "specs": {
      "tdp_rating": 450,
      "length_mm": 340,
      "slot_width": 3.5,
      "required_pcie_version": "4.0",
      "power_connectors": "16-pin",
      "power_connector_count": 1,
      "vram_gb": 24,
      "vram_type": "GDDR6X"
    }
  },
  {
    "name": "PowerColor Fighter Radeon RX 6600",
    "brand": "PowerColor",
    "type": "gpu",
    "price": 279.99,
    "stock": 25,
    "ratings": [],
    "specs": {
      "tdp_rating": 132,
      "length_mm": 220,
      "slot_width": 2,
      "required_pcie_version": "4.0",
      "power_connectors": "8-pin",
      "power_connector_count": 1,
      "vram_gb": 8,
      "vram_type": "GDDR6"
    }
  },
  {
    "name": "ZOTAC Gaming GeForce RTX 3060 Twin Edge",
    "brand": "ZOTAC",
    "type": "gpu",
    "price": 349.99,
    "stock": 15,
    "ratings": [],
    "specs": {
      "tdp_rating": 170,
      "length_mm": 224,
      "slot_width": 2,
      "required_pcie_version": "4.0",
      "power_connectors": "8-pin",
      "power_connector_count": 1,
      "vram_gb": 12,
      "vram_type": "GDDR6"
    }
  },
  {
    "name": "ASRock Challenger Radeon RX 7900 GRE",
    "brand": "ASRock",
    "type": "gpu",
    "price": 799.99,
    "stock": 7,
    "ratings": [],
    "specs": {
      "tdp_rating": 260,
      "length_mm": 295,
      "slot_width": 2.5,
      "required_pcie_version": "4.0",
      "power_connectors": "8-pin",
      "power_connector_count": 2,
      "vram_gb": 16,
      "vram_type": "GDDR6"
    }
  },
  {
    "name": "MSI GeForce RTX 4070 Super Ventus 3X",
    "brand": "MSI",
    "type": "gpu",
    "price": 829.99,
    "stock": 10,
    "ratings": [],
    "specs": {
      "tdp_rating": 220,
      "length_mm": 308,
      "slot_width": 2.5,
      "required_pcie_version": "4.0",
      "power_connectors": "16-pin",
      "power_connector_count": 1,
      "vram_gb": 12,
      "vram_type": "GDDR6X"
    }
  },
  {
    "name": "EVGA GeForce RTX 3060 XC Gaming",
    "brand": "EVGA",
    "type": "gpu",
    "price": 359.99,
    "stock": 18,
    "ratings": [],
    "specs": {
      "tdp_rating": 170,
      "length_mm": 201,
      "slot_width": 2,
      "required_pcie_version": "4.0",
      "power_connectors": "8-pin",
      "power_connector_count": 1,
      "vram_gb": 12,
      "vram_type": "GDDR6"
    }
  },
  {
    "name": "MSI B760 Tomahawk WiFi",
    "brand": "MSI",
    "type": "motherboard",
    "price": 249.99,
    "stock": 10,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "form_factor": "ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 6800,
      "max_memory_capacity": 192,
      "memory_slots": 4,
      "pcie_version": "5.0",
      "m2_slots": 3,
      "sata_ports": 6
    }
  },
  {
    "name": "ASUS ROG Strix Z790-H",
    "brand": "ASUS",
    "type": "motherboard",
    "price": 379.99,
    "stock": 8,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "form_factor": "ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 7800,
      "max_memory_capacity": 128,
      "memory_slots": 4,
      "pcie_version": "5.0",
      "m2_slots": 4,
      "sata_ports": 6
    }
  },
  {
    "name": "ASRock B650M Pro RS",
    "brand": "ASRock",
    "type": "motherboard",
    "price": 189.99,
    "stock": 18,
    "ratings": [],
    "specs": {
      "socket": "AM5",
      "form_factor": "Micro-ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 6400,
      "max_memory_capacity": 128,
      "memory_slots": 4,
      "pcie_version": "4.0",
      "m2_slots": 2,
      "sata_ports": 4
    }
  },
  {
    "name": "Gigabyte B650 AORUS Elite AX",
    "brand": "Gigabyte",
    "type": "motherboard",
    "price": 279.99,
    "stock": 12,
    "ratings": [],
    "specs": {
      "socket": "AM5",
      "form_factor": "ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 6600,
      "max_memory_capacity": 192,
      "memory_slots": 4,
      "pcie_version": "4.0",
      "m2_slots": 3,
      "sata_ports": 4
    }
  },
  {
    "name": "MSI PRO B760M-A",
    "brand": "MSI",
    "type": "motherboard",
    "price": 169.99,
    "stock": 15,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "form_factor": "Micro-ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 6400,
      "max_memory_capacity": 128,
      "memory_slots": 4,
      "pcie_version": "4.0",
      "m2_slots": 2,
      "sata_ports": 4
    }
  },
  {
    "name": "ASUS Prime B760M-A",
    "brand": "ASUS",
    "type": "motherboard",
    "price": 159.99,
    "stock": 20,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "form_factor": "Micro-ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 7200,
      "max_memory_capacity": 128,
      "memory_slots": 4,
      "pcie_version": "4.0",
      "m2_slots": 2,
      "sata_ports": 4
    }
  },
  {
    "name": "MSI B550-A PRO",
    "brand": "MSI",
    "type": "motherboard",
    "price": 149.99,
    "stock": 22,
    "ratings": [],
    "specs": {
      "socket": "AM4",
      "form_factor": "ATX",
      "memory_type": "DDR4",
      "max_memory_speed": 4400,
      "max_memory_capacity": 128,
      "memory_slots": 4,
      "pcie_version": "4.0",
      "m2_slots": 2,
      "sata_ports": 6
    }
  },
  {
    "name": "Gigabyte B550 AORUS Elite",
    "brand": "Gigabyte",
    "type": "motherboard",
    "price": 179.99,
    "stock": 14,
    "ratings": [],
    "specs": {
      "socket": "AM4",
      "form_factor": "ATX",
      "memory_type": "DDR4",
      "max_memory_speed": 4733,
      "max_memory_capacity": 128,
      "memory_slots": 4,
      "pcie_version": "4.0",
      "m2_slots": 2,
      "sata_ports": 6
    }
  },
  {
    "name": "ASRock Z790 PG Lightning",
    "brand": "ASRock",
    "type": "motherboard",
    "price": 219.99,
    "stock": 12,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "form_factor": "ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 6800,
      "max_memory_capacity": 128,
      "memory_slots": 4,
      "pcie_version": "5.0",
      "m2_slots": 4,
      "sata_ports": 4
    }
  },
  {
    "name": "ASRock B760M Pro RS",
    "brand": "ASRock",
    "type": "motherboard",
    "price": 144.99,
    "stock": 25,
    "ratings": [],
    "specs": {
      "socket": "LGA1700",
      "form_factor": "Micro-ATX",
      "memory_type": "DDR5",
      "max_memory_speed": 7200,
      "max_memory_capacity": 192,
      "memory_slots": 4,
      "pcie_version": "4.0",
      "m2_slots": 2,
      "sata_ports": 4
    }
  },
  {
    "name": "Corsair Vengeance RGB 32GB DDR5",
    "brand": "Corsair",
    "type": "ram",
    "price": 159.99,
    "stock": 35,
    "ratings": [],
    "specs": {
      "memory_type": "DDR5",
      "capacity_per_module_gb": 16,
      "module_count": 2,
      "total_capacity_gb": 32,
      "speed": 6000,
      "cas_latency": 30
    }
  },
  {
    "name": "TEAMGROUP T-Force Vulcan Z 32GB DDR4",
    "brand": "TEAMGROUP",
    "type": "ram",
    "price": 89.99,
    "stock": 28,
    "ratings": [],
    "specs": {
      "memory_type": "DDR4",
      "capacity_per_module_gb": 16,
      "module_count": 2,
      "total_capacity_gb": 32,
      "speed": 3200,
      "cas_latency": 16
    }
  },
  {
    "name": "G.Skill Ripjaws V 16GB DDR4",
    "brand": "G.Skill",
    "type": "ram",
    "price": 54.99,
    "stock": 45,
    "ratings": [],
    "specs": {
      "memory_type": "DDR4",
      "capacity_per_module_gb": 8,
      "module_count": 2,
      "total_capacity_gb": 16,
      "speed": 3200,
      "cas_latency": 16
    }
  },
  {
    "name": "Kingston Fury Beast 32GB DDR5",
    "brand": "Kingston",
    "type": "ram",
    "price": 139.99,
    "stock": 22,
    "ratings": [],
    "specs": {
      "memory_type": "DDR5",
      "capacity_per_module_gb": 16,
      "module_count": 2,
      "total_capacity_gb": 32,
      "speed": 5600,
      "cas_latency": 40
    }
  },
  {
    "name": "Corsair Vengeance LPX 32GB DDR4",
    "brand": "Corsair",
    "type": "ram",
    "price": 109.99,
    "stock": 30,
    "ratings": [],
    "specs": {
      "memory_type": "DDR4",
      "capacity_per_module_gb": 16,
      "module_count": 2,
      "total_capacity_gb": 32,
      "speed": 3200,
      "cas_latency": 16
    }
  },
  {
    "name": "G.Skill Trident Z5 RGB 32GB DDR5",
    "brand": "G.Skill",
    "type": "ram",
    "price": 179.99,
    "stock": 18,
    "ratings": [],
    "specs": {
      "memory_type": "DDR5",
      "capacity_per_module_gb": 16,
      "module_count": 2,
      "total_capacity_gb": 32,
      "speed": 6000,
      "cas_latency": 36
    }
  },
  {
    "name": "Patriot Viper Steel 16GB DDR4",
    "brand": "Patriot",
    "type": "ram",
    "price": 49.99,
    "stock": 40,
    "ratings": [],
    "specs": {
      "memory_type": "DDR4",
      "capacity_per_module_gb": 8,
      "module_count": 2,
      "total_capacity_gb": 16,
      "speed": 3200,
      "cas_latency": 16
    }
  },
  {
    "name": "Crucial Pro 32GB DDR5",
    "brand": "Crucial",
    "type": "ram",
    "price": 119.99,
    "stock": 25,
    "ratings": [],
    "specs": {
      "memory_type": "DDR5",
      "capacity_per_module_gb": 16,
      "module_count": 2,
      "total_capacity_gb": 32,
      "speed": 5600,
      "cas_latency": 46
    }
  },
  {
    "name": "Corsair Vengeance RGB 64GB DDR5",
    "brand": "Corsair",
    "type": "ram",
    "price": 279.99,
    "stock": 8,
    "ratings": [],
    "specs": {
      "memory_type": "DDR5",
      "capacity_per_module_gb": 32,
      "module_count": 2,
      "total_capacity_gb": 64,
      "speed": 6000,
      "cas_latency": 40
    }
  },
  {
    "name": "TEAMGROUP T-Force Delta RGB 32GB DDR5",
    "brand": "TEAMGROUP",
    "type": "ram",
    "price": 149.99,
    "stock": 20,
    "ratings": [],
    "specs": {
      "memory_type": "DDR5",
      "capacity_per_module_gb": 16,
      "module_count": 2,
      "total_capacity_gb": 32,
      "speed": 6000,
      "cas_latency": 38
    }
  },
  {
    "name": "Samsung 980 Pro 1TB NVMe SSD",
    "brand": "Samsung",
    "type": "storage",
    "price": 129.99,
    "stock": 40,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 1000,
      "interface": "NVMe",
      "form_factor": "M.2 2280",
      "requires_m2_slot": True,
      "requires_sata_port": False
    }
  },
  {
    "name": "Western Digital Blue 1TB SATA SSD",
    "brand": "Western Digital",
    "type": "storage",
    "price": 89.99,
    "stock": 35,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 1000,
      "interface": "SATA",
      "form_factor": "2.5 inch",
      "requires_m2_slot": False,
      "requires_sata_port": True
    }
  },
  {
    "name": "Seagate Barracuda 2TB HDD",
    "brand": "Seagate",
    "type": "storage",
    "price": 79.99,
    "stock": 50,
    "ratings": [],
    "specs": {
      "storage_type": "HDD",
      "capacity_gb": 2000,
      "interface": "SATA",
      "form_factor": "3.5 inch",
      "requires_m2_slot": False,
      "requires_sata_port": True
    }
  },
  {
    "name": "WD Black SN850X 2TB NVMe SSD",
    "brand": "Western Digital",
    "type": "storage",
    "price": 199.99,
    "stock": 22,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 2000,
      "interface": "NVMe",
      "form_factor": "M.2 2280",
      "requires_m2_slot": True,
      "requires_sata_port": False
    }
  },
  {
    "name": "Crucial P3 Plus 500GB NVMe SSD",
    "brand": "Crucial",
    "type": "storage",
    "price": 49.99,
    "stock": 55,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 500,
      "interface": "NVMe",
      "form_factor": "M.2 2280",
      "requires_m2_slot": True,
      "requires_sata_port": False
    }
  },
  {
    "name": "Samsung 870 EVO 500GB SATA SSD",
    "brand": "Samsung",
    "type": "storage",
    "price": 59.99,
    "stock": 30,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 500,
      "interface": "SATA",
      "form_factor": "2.5 inch",
      "requires_m2_slot": False,
      "requires_sata_port": True
    }
  },
  {
    "name": "Kingston KC3000 1TB NVMe SSD",
    "brand": "Kingston",
    "type": "storage",
    "price": 119.99,
    "stock": 28,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 1000,
      "interface": "NVMe",
      "form_factor": "M.2 2280",
      "requires_m2_slot": True,
      "requires_sata_port": False
    }
  },
  {
    "name": "Seagate FireCuda 530 1TB NVMe SSD",
    "brand": "Seagate",
    "type": "storage",
    "price": 159.99,
    "stock": 15,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 1000,
      "interface": "NVMe",
      "form_factor": "M.2 2280",
      "requires_m2_slot": True,
      "requires_sata_port": False
    }
  },
  {
    "name": "TEAMGROUP MP33 1TB NVMe SSD",
    "brand": "TEAMGROUP",
    "type": "storage",
    "price": 69.99,
    "stock": 45,
    "ratings": [],
    "specs": {
      "storage_type": "SSD",
      "capacity_gb": 1000,
      "interface": "NVMe",
      "form_factor": "M.2 2280",
      "requires_m2_slot": True,
      "requires_sata_port": False
    }
  },
  {
    "name": "Western Digital Red 4TB HDD",
    "brand": "Western Digital",
    "type": "storage",
    "price": 149.99,
    "stock": 20,
    "ratings": [],
    "specs": {
      "storage_type": "HDD",
      "capacity_gb": 4000,
      "interface": "SATA",
      "form_factor": "3.5 inch",
      "requires_m2_slot": False,
      "requires_sata_port": True
    }
  },
  {
    "name": "Corsair RM750e 750W Gold",
    "brand": "Corsair",
    "type": "psu",
    "price": 139.99,
    "stock": 25,
    "ratings": [],
    "specs": {
        "wattage": 750,
        "efficiency": "Gold",
        "modular": "Full",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 3,
            "has_12vhpwr": False,
            "sata_power": 6,
            "molex": 4
        }
    }
},
{
    "name": "EVGA 600 W1 600W",
    "brand": "EVGA",
    "type": "psu",
    "price": 69.99,
    "stock": 35,
    "ratings": [],
    "specs": {
        "wattage": 600,
        "efficiency": "White",
        "modular": "Non-modular",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 1,
            "pcie_6_2_pin": 2,
            "has_12vhpwr": False,
            "sata_power": 4,
            "molex": 3
        }
    }
},
{
    "name": "Seasonic Focus Plus 850W Gold",
    "brand": "Seasonic",
    "type": "psu",
    "price": 189.99,
    "stock": 18,
    "ratings": [],
    "specs": {
        "wattage": 850,
        "efficiency": "Gold",
        "modular": "Full",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 4,
            "has_12vhpwr": False,
            "sata_power": 8,
            "molex": 5
        }
    }
},
{
    "name": "MSI MPG A1000G 1000W Gold",
    "brand": "MSI",
    "type": "psu",
    "price": 249.99,
    "stock": 12,
    "ratings": [],
    "specs": {
        "wattage": 1000,
        "efficiency": "Gold",
        "modular": "Full",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 4,
            "has_12vhpwr": True,
            "sata_power": 8,
            "molex": 4
        }
    }
},
{
    "name": "Corsair RM850x 850W Gold",
    "brand": "Corsair",
    "type": "psu",
    "price": 179.99,
    "stock": 20,
    "ratings": [],
    "specs": {
        "wattage": 850,
        "efficiency": "Gold",
        "modular": "Full",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 4,
            "has_12vhpwr": False,
            "sata_power": 8,
            "molex": 4
        }
    }
},
{
    "name": "Thermaltake Smart 500W",
    "brand": "Thermaltake",
    "type": "psu",
    "price": 49.99,
    "stock": 40,
    "ratings": [],
    "specs": {
        "wattage": 500,
        "efficiency": "White",
        "modular": "Non-modular",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 1,
            "pcie_6_2_pin": 1,
            "has_12vhpwr": False,
            "sata_power": 4,
            "molex": 2
        }
    }
},
{
    "name": "Corsair RM1000e 1000W Gold",
    "brand": "Corsair",
    "type": "psu",
    "price": 219.99,
    "stock": 15,
    "ratings": [],
    "specs": {
        "wattage": 1000,
        "efficiency": "Gold",
        "modular": "Full",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 4,
            "has_12vhpwr": True,
            "sata_power": 8,
            "molex": 4
        }
    }
},
{
    "name": "EVGA SuperNOVA 750 G5",
    "brand": "EVGA",
    "type": "psu",
    "price": 159.99,
    "stock": 22,
    "ratings": [],
    "specs": {
        "wattage": 750,
        "efficiency": "Gold",
        "modular": "Full",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 4,
            "has_12vhpwr": False,
            "sata_power": 6,
            "molex": 3
        }
    }
},
{
    "name": "be quiet! Pure Power 12 M 750W",
    "brand": "be quiet!",
    "type": "psu",
    "price": 149.99,
    "stock": 18,
    "ratings": [],
    "specs": {
        "wattage": 750,
        "efficiency": "Gold",
        "modular": "Full",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 3,
            "has_12vhpwr": True,
            "sata_power": 7,
            "molex": 2
        }
    }
},
{
    "name": "Cooler Master MWE 650 Bronze",
    "brand": "Cooler Master",
    "type": "psu",
    "price": 89.99,
    "stock": 30,
    "ratings": [],
    "specs": {
        "wattage": 650,
        "efficiency": "Bronze",
        "modular": "Semi-modular",
        "form_factor": "ATX",
        "connectors": {
            "cpu_4_4_pin": 2,
            "pcie_6_2_pin": 2,
            "has_12vhpwr": False,
            "sata_power": 6,
            "molex": 3
        }
    }
}
]

existingNames = set(products_col.distinct("name"))
newProducts = [product for product in products if product["name"] not in existingNames]

if newProducts:
  result = products_col.insert_many(newProducts)
  print("Database seeded successfully.")
else:
  print("Database already seeded.")
