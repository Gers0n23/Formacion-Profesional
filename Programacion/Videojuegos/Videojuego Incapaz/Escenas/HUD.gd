extends CanvasLayer

@onready var health_bar = $health_ProgressBar
@onready var player = null

func _ready():
	var player_path = "res://Escenas/player/CharacterBody2D.tscn"  # Ajusta la ruta si es necesario
	player = get_tree().get_nodes_in_group("player")[0] if get_tree().has_group("player") else null
	if player:
		health_bar.max_value = player.health
		health_bar.value = player.health
	else:
		print("Error: No se encontró el nodo del jugador.")

func _process(_delta):
	if player:
		health_bar.value = player.health
