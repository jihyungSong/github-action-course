package humancat

import "fmt"

func Hello(name string) string {
  message := fmt.Sprintf("Hell, %s", name)
  return message
}
