extends ProgressBar


var maxvalor:int
var damage:int

func _ready():
	maxvalor = 100
	
func DisminuirVida():
	value-=damage
