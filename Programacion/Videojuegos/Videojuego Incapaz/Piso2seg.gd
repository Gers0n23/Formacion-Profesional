extends Node2D  # Nodo principal: Piso2seg

@onready var collision_shape = $"StaticBody2D/CollisionShape2D"
@onready var image_node = $"StaticBody2D/Sprite2D"  # Reemplaza por el nombre y ruta de tu imagen
@onready var image_node1 = $"StaticBody2D/Inacap"

func _ready():
	if collision_shape and image_node:
		await get_tree().create_timer(2).timeout
		collision_shape.disabled = true  # Desactiva la colisión
		await get_tree().create_timer(1).timeout
		image_node.visible = false  
		image_node1.visible = false      
	else:
		print("CollisionShape2D o imagen no encontrados.")
