package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

const url = "https://lco.dev" //change to any url that is live

func main() {
	fmt.Println("LCO web Request")

	response, err := http.Get(url)

	if err != nil {
		panic(err)
	}

	fmt.Printf("Response is of type: %T", response)
	defer response.Body.Close() // caller's responsibility to close the connection

	databytes, err := ioutil.ReadAll(response.Body)

	if err != nil {
		panic(err)
	}

	content := string(databytes)

	fmt.Println(content)

}
