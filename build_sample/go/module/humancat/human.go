package humancat

type Human struct {
	name   string
	age    int
}

func (h Human) get_name() string {
	return h.name 
}

func (h Human) set_name(name string) {
	h.name = name
}

func (h Human) get_age() int {
	return h.age 
}

func (h Human) set_age(age int) {
	h.age = int
}

func (h Human) get_info() string {
	return "My name is %s and %d years old." % (self.name, self.age)
}
