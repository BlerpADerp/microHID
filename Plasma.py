{
	"format_version": "1.16.0",
	"minecraft:geometry": [
		{
			"description": {
				"identifier": "geometry.plasma",
				"texture_width": 32,
				"texture_height": 32,
				"visible_bounds_width": 2,
				"visible_bounds_height": 1.5,
				"visible_bounds_offset": [0, 0.25, 0]
			},
			"bones": [
				{
					"name": "root_item",
					"pivot": [0, 0, 0],
					"binding": "q.item_slot_to_bone_name(c.item_slot)",
					"cubes": [
						{"origin": [-4.5, 0, 0.5], "size": [5, 5, 5], "uv": [0, 0]},
						{"origin": [-5.4, 4, -1.7], "size": [6.8, 2, 7], "pivot": [0, 2, -1.2], "rotation": [-37.5, 0, 0], "uv": [-2, 20]},
						{"origin": [-5, 2, -0.2], "size": [5.9, 2, 6.1], "pivot": [0, 0, -0.2], "rotation": [-2.5, 0, 0], "uv": [0, 22]},
						{"origin": [-5.5, 9, 2.4], "size": [7, 2, 7], "pivot": [0, 7, 2.9], "rotation": [-137.5, 0, 0], "uv": [-3, 20]}
					]
				}
			]
		}
	]
}
{
    "format_version": "1.10.0",
    "plasma_gun": {
        "shoot_behavior": {
            "launch_speed": 30,
            "start_position": {
                "relative_to": "gun",
                "coordinates": [0, 0, 0]
            },
            "texture": "texture (8).png",
            "particles": {
                "type": "blue_glow",
                "emission_rate": 50,
                "particle_lifetime": 1.5,
                "color": {
                    "start": [0, 0, 255, 255],
                    "end": [0, 0, 128, 128]
                },
                "size": {
                    "start": 0.5,
                    "end": 0.2
                },
                "motion": {
                    "spread": 15,
                    "speed": [5, 10]
                }
            }
        },
        "trigger_event": {
            "on_receive": "shoot",
            "execute_action": "shoot_behavior"
        }
    }
}
class Plasma:
    def __init__(self):
        self.launch_speed = 30  # Speed of plasma
        self.texture = "texture (8).png"  # Visual representation of the plasma
        self.explosion_damage = 2.5  # Damage dealt when hitting an object
        self.living_damage = 4.5 * 2  # 4.5 hearts = 9 health points (1 heart = 2 health points)

    def on_hit(self, target):
        """
        Handles the plasma's behavior when it hits something.
        """
        if target.is_alive:  # Assuming target has an `is_alive` property
            print(f"Hit living target! Inflicting {self.living_damage} damage.")
            target.health -= self.living_damage
        else:
            print("Hit object! Triggering explosion.")
            self.explode(target)

    def explode(self, target):
        """
        Triggers an explosion when the plasma hits an object.
        """
        print(f"Explosion at {target.position}! Inflicting {self.explosion_damage} damage.")
        # Apply explosion logic here (e.g., area of effect damage)
        # Assuming you have a list of nearby objects to damage

# Example usage
class Target:
    def __init__(self, is_alive, health, position):
        self.is_alive = is_alive
        self.health = health
        self.position = position

# Create plasma
plasma = Plasma()

# Simulate hitting a living target
living_target = Target(is_alive=True, health=20, position=(10, 10))
plasma.on_hit(living_target)
print(f"Living target's health: {living_target.health}")

# Simulate hitting an object
object_target = Target(is_alive=False, health=0, position=(15, 15))
plasma.on_hit(object_target)
