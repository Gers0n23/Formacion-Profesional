extends Control




func _on_plai_pressed():
	get_tree().change_scene_to_file("res://Escenas/Exterior.tscn")


func _on_optiones_pressed():
	get_tree().change_scene_to_file("res://Escenas/Lobby/optiones.tscn")


func _on_pajuera_pressed():
	get_tree().quit()
	
