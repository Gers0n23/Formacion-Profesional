extends CanvasLayer

@onready var background_fade = $BackgroundFade  # Accede al ColorRect
@onready var animation_player = $AnimationPlayer
@onready var timer = $Timer

func _ready():
	timer.start()  # Inicia el temporizador para el retraso
	background_fade.modulate.a = 0  # Rojo y transparente
	background_fade.z_index = 1  # Asegura que el fondo esté encima de otros elementos
	
	animation_player.play("fade_in")  # Inicia la animación

func _on_retry_button_pressed():
	get_tree().change_scene_to_file("res://Escenas/Exterior.tscn")
	queue_free()
func _on_exit_button_pressed():
	get_tree().change_scene_to_file("res://Escenas/Lobby/control.tscn")
	queue_free()
