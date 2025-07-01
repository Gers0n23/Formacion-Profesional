extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
var guard_dialogues = [
	"¡A formar de nuevo, campeón!",
	"Eso no es tu huella, amigo.",
	"¡Vuelve a intentarlo, con ganas esta vez!"
]

func show_guard():
	guard_sprite.visible = true
	var dialogue = guard_dialogues[randi() % guard_dialogues.size()]
	$Guard/Label.text = dialogue
	await get_tree().create_timer(2). timeout
	reset_game()
	guard_sprite.visible = false
