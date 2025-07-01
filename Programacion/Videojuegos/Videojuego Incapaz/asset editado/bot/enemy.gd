extends CharacterBody2D

@export var speed := 400.0
@export var gravity := 18000.0
@export var attack_damage := 10
@export var health := 50
@export var attack_duration := 1.0
@export var hurt_duration := 0.5
@export var knockback_strength := 300.0
@export var damage_interval := 0.8  # Intervalo entre cada daño al jugador

var is_alive := true
var is_attacking := false
var is_hurt := false
var hurt_timer := 0.0
var attack_timer := 0.0
var damage_timer := 0.0  # Timer para aplicar daño repetido

@onready var animated_sprite = $enemysprite
@onready var attack_range = $AttackRange  # Nodo del rango de ataque
@onready var player = null

func _ready():
	add_to_group("enemy")
	player = get_tree().get_nodes_in_group("player")[0] if get_tree().has_group("player") else null

	# Conexión de señales con prevención de conexiones repetidas
	if not attack_range.is_connected("body_entered", Callable(self, "_on_attack_range_body_entered")):
		attack_range.connect("body_entered", Callable(self, "_on_attack_range_body_entered"))
	if not attack_range.is_connected("body_exited", Callable(self, "_on_attack_range_body_exited")):
		attack_range.connect("body_exited", Callable(self, "_on_attack_range_body_exited"))

func _physics_process(delta):
	if is_alive:
		if is_hurt:
			handle_hurt(delta)
		elif is_attacking:
			handle_attack(delta)
		else:
			handle_movement(delta)

		# Si el jugador está dentro del rango y el enemigo está atacando, aplica daño
		if is_attacking and is_within_attack_range() and not is_hurt:  # Impide el daño si está herido
			damage_timer -= delta
			if damage_timer <= 0:
				apply_damage_to_player()
				damage_timer = damage_interval  # Reinicia el temporizador de daño
	else:
		if animated_sprite.animation != "death":
			animated_sprite.play("death")


func handle_movement(delta):
	if not player:
		return

	var direction_to_player = player.global_position - global_position
	velocity.x = direction_to_player.normalized().x * speed
	animated_sprite.play("walk")
	animated_sprite.flip_h = velocity.x < 0
	velocity.y += gravity * delta
	move_and_slide()

func handle_attack(delta):
	attack_timer -= delta
	if attack_timer <= 0:
		if is_within_attack_range():
			start_attack()
		else:
			is_attacking = false
			if animated_sprite.animation != "idle":
				animated_sprite.play("idle")

func start_attack():
	if is_attacking or is_hurt:  # No deja atacar si está herido o atacando
		return
	is_attacking = true
	attack_timer = attack_duration
	damage_timer = damage_interval  # Reinicia el temporizador de daño
	animated_sprite.play("attack")
	print("Enemigo atacando al jugador")

	# Aplicar daño al jugador después de 0.5 segundos
	await get_tree().create_timer(0.5).timeout
	if player and player.is_in_group("player") and is_within_attack_range():
		apply_damage_to_player()


func apply_damage_to_player():
	# Aplica el daño al jugador si está dentro del rango
	if player and player.is_in_group("player"):
		if player.has_method("take_damage"):
			player.take_damage(attack_damage)
			print("Jugador recibió daño:", attack_damage)


func is_within_attack_range() -> bool:
	# Verifica si el jugador aún está en el rango de ataque
	return player and attack_range.get_overlapping_bodies().has(player)

func handle_hurt(delta):
	hurt_timer -= delta
	if hurt_timer <= 0:
		is_hurt = false
		if animated_sprite.animation != "idle":
			animated_sprite.play("idle")

	velocity.y += gravity * delta
	move_and_slide()

func take_damage(amount, knockback_direction):
	if is_alive and not is_hurt:
		health -= amount
		if health > 0:
			is_hurt = true
			hurt_timer = hurt_duration
			if animated_sprite.animation != "hurt":
				animated_sprite.play("hurt")
			print("Enemigo recibió daño:", amount, "Salud restante:", health)

			# Aplicar empuje
			velocity.x = knockback_direction * knockback_strength
		else:
			print("Enemigo muerto")
			is_alive = false
			if animated_sprite.animation != "death":
				animated_sprite.play("death")
			await get_tree().create_timer(1).timeout  # Esperar antes de eliminar al enemigo
			queue_free()

# Señales para manejar el rango de ataque
func _on_attack_range_body_entered(body):
	if body.is_in_group("player"):  # Verificar que es el jugador
		print("Jugador entró en rango de ataque")
		start_attack()

func _on_attack_range_body_exited(body):
	if body.is_in_group("player"):  # Verificar que es el jugador
		print("Jugador salió del rango de ataque")
		is_attacking = false
		damage_timer = 0  # Detiene el temporizador de daño

