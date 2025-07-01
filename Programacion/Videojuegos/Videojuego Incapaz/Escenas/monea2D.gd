extends Area2D

@onready var player = $"../AudioStreamPlayer"



func _on_body_entered(_body):
	player.play() 
	queue_free()
