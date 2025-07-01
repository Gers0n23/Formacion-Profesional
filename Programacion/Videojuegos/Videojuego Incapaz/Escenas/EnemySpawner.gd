extends Node2D

@export var spawn_interval := 7.0  # Intervalo entre apariciones
@export var enemy_scene: PackedScene  # La escena del enemigo
@export var spawn_margin := 600  # Margen fuera de la pantalla donde aparecerán los enemigos

var spawn_zones: Array = []  # Zonas de aparición (las asignamos en _ready())
var spawn_timer := 0.0

func _ready():
	# Recuperamos las zonas de spawn desde la escena Exterior
	var exterior_scene = get_parent()  # Asumimos que "EnemySpawner" es hijo de "Exterior"
	
	# Asegurarnos de que hay nodos de tipo Node2D en la escena Exterior
	spawn_zones = []
	for node in exterior_scene.get_children():
		if node is Node2D:
			spawn_zones.append(node)  # Agregamos nodos de tipo Node2D a spawn_zones
	
	spawn_timer = spawn_interval

func _process(delta):
	spawn_timer -= delta
	if spawn_timer <= 0:
		spawn_enemy()
		spawn_timer = spawn_interval

func spawn_enemy():
	if not enemy_scene:
		print("Enemy scene no asignada")
		return

	if spawn_zones.size() == 0:
		print("No hay zonas de spawn definidas.")
		return

	# Seleccionamos una zona aleatoria de las zonas disponibles
	var spawn_zone = spawn_zones[randi() % spawn_zones.size()]
	
	# Generar una posición aleatoria alrededor de la zona de spawn
	var spawn_position = spawn_zone.position + Vector2(
		randf_range(-spawn_margin, spawn_margin),
		randf_range(-spawn_margin, spawn_margin)
	)

	# Instanciar el enemigo
	var enemy_instance = enemy_scene.instantiate()
	enemy_instance.position = spawn_position
	add_child(enemy_instance)
