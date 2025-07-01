extends CharacterBody2D

# Variables de movimiento
@export var speed := 800.0
var original_speed := speed
@export var jump_force := -5000.0
@export var gravity := 15000.0
@export var knockback_strength := 300.0
@export var game_over_scene = preload("res://Escenas/game_over.tscn")
# Variables de combate y estado
var is_attacking := false
@export var attack_damage := 20
@export var attack_duration := 0.5
var max_health := 100
var health := max_health
var is_alive := true

# Dirección del personaje
var facing_right := true

# Nodo de animación y área de golpe
@onready var animated_sprite = $AnimatedSprite2D2
@onready var hitbox = $Hitbox

func _ready():
	# Conectar la señal del área de golpe
	hitbox.connect("body_entered", Callable(self, "_on_Hitbox_body_entered"))
	hitbox.monitoring = false  # Desactivado por defecto

func _physics_process(delta):
	if is_alive:
		handle_movement(delta)
		handle_attack()
		update_hitbox_position()
	else:
		animated_sprite.play("death")

# Manejo de movimiento y gravedad
func handle_movement(delta):
	if !is_attacking:
		if Input.is_action_pressed("ui_right"):
			velocity.x = speed
			facing_right = true
			if is_on_floor():
				animated_sprite.play("walk")
		elif Input.is_action_pressed("ui_left"):
			velocity.x = -speed
			facing_right = false
			if is_on_floor():
				animated_sprite.play("walk")
		elif is_on_floor():
			velocity.x = 0
			animated_sprite.play("idle")

	# Actualizar la dirección del sprite
	animated_sprite.flip_h = not facing_right

	# Aplicar gravedad
	velocity.y += gravity * delta

	# Saltar
	if Input.is_action_just_pressed("jump") and is_on_floor() and !is_attacking:
		velocity.y = jump_force
		animated_sprite.play("jump")

	move_and_slide()
# Método para curar al jugador
func heal(amount):
	health = min(health + amount, max_health)
	print("Salud del jugador:", health)

# Método para establecer la velocidad temporalmente
func set_speed(new_speed):
	speed = new_speed
	print("Nueva velocidad del jugador:", speed)

# Método para restablecer la velocidad original
func reset_speed():
	speed = original_speed
	print("Velocidad del jugador restablecida:", speed)
# Manejo de ataque
func handle_attack():
	if Input.is_action_just_pressed("attack") and !is_attacking:
		is_attacking = true
		hitbox.monitoring = true  # Activa el área de golpe
		animated_sprite.play("attack")
		print("Jugador está atacando")
		await get_tree().create_timer(attack_duration).timeout
		is_attacking = false
		hitbox.monitoring = false  # Desactiva el área de golpe
func update_hitbox_position():
	# Define un desplazamiento horizontal
	var hitbox_offset = Vector2(40, 0)  # Ajusta este valor según el tamaño del personaje
	if facing_right:
		hitbox.position = hitbox_offset  # Posición a la derecha
	else:
		hitbox.position = -hitbox_offset  # Posición a la izquierda
# Recibir daño
func take_damage(damage: int):
	if is_alive:
		health -= damage
		if health > 0:
			print("Enemigo recibió daño:", damage, "Salud restante:", health)
			animated_sprite.play("hurt")  # Se reproduce la animación de herida
			
			
		else:
			print("Enemigo muerto")
			is_alive = false
			animated_sprite.play("death")  # Se reproduce la animación de muerte
			
func handle_game_over():
	var game_over_instance = game_over_scene.instantiate()
	get_tree().get_root().add_child(game_over_instance)


func _on_hitbox_body_entered(body):
	if is_attacking and body.is_in_group("enemy"):  # Verifica que es un enemigo
		var knockback_direction = 1 if facing_right else -5  # Dirección del empuje
		body.take_damage(attack_damage, knockback_direction)  # Llamamos a la función take_damage del enemigo
		print("Golpeaste al enemigo:", body.name)

