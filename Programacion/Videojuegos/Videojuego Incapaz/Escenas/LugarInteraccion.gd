extends Area2D

@export var porteria_scene: PackedScene

@onready var arrow_sprite = $ArrowSprite

var is_player_near = false
var player = null

func _ready():
	arrow_sprite.visible = false
	disconnect_signals()
	connect("body_entered", Callable(self, "_on_body_entered"))
	connect("body_exited", Callable(self, "_on_body_exited"))

func disconnect_signals():
	if is_connected("body_entered", Callable(self, "_on_body_entered")):
		disconnect("body_entered", Callable(self, "_on_body_entered"))
	if is_connected("body_exited", Callable(self, "_on_body_exited")):
		disconnect("body_exited", Callable(self, "_on_body_exited"))

func _on_body_entered(body):
	if body.is_in_group("player"):
		is_player_near = true
		player = body
		arrow_sprite.visible = true

func _on_body_exited(body):
	if body.is_in_group("player"):
		is_player_near = false
		player = null
		arrow_sprite.visible = false

func _process(_delta):
	if is_player_near and Input.is_action_just_pressed("ui_up"):
		load_porteria_scene()

func load_porteria_scene():
	if porteria_scene:
		var new_scene = porteria_scene.instantiate()
		if new_scene:
			get_tree().root.add_child(new_scene)  # Agrega la nueva escena al árbol
			get_tree().current_scene.queue_free()  # Libera la escena actual
			get_tree().current_scene = new_scene  # Establece la nueva escena como actual
