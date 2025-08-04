
main.go
```go
package main
import (
    "fmt"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/iam"
)
func main() {
    svc := iam.New(session.Must(session.NewSession()))
    users, _ := svc.ListUsers(&iam.ListUsersInput{})
    for _, u := range users.Users {
        fmt.Println(*u.UserName)
    }
}