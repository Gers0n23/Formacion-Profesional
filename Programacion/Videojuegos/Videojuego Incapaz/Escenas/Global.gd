extends Node

var current_scene: Node = null

func change_scene(new_scene_path: String):
	if current_scene:
		current_scene.queue_free()
	var new_scene = load(new_scene_path).instantiate()
	get_tree().root.add_child(new_scene)
	current_scene = new_scene
