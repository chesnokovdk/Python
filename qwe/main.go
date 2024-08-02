package main

import (
	// "encoding/json"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

type MyStruct struct {
	Location struct {
		Name      string  `json:"name"`
		Region    string  `json:"region"`
		Country   string  `json:"country"`
		Lat       float64 `json:"lat"`
		Lon       float64 `json:"lon"`
		Localtime string  `json:"localtime"`
	} `json:"location"`
	Current struct {
		LastUpdatedEpoch int     `json:"last_updated_epoch"`
		LastUpdated      string  `json:"last_updated"`
		TempC            float64 `json:"temp_c"`
		IsDay            int     `json:"is_day"`
	} `json:"current"`
}

func main() {
	api := "3458debc61cf4d9f9ca144424243107"
	city := "Moscow"
	url := fmt.Sprintf("http://api.weatherapi.com/v1/current.json?key=%s&q=%s", api, city)

	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	bodyBytes, err := io.ReadAll(resp.Body)
	// fmt.Println(string(bodyBytes))
	if err != nil {
		log.Println(err)
	}
	b := &MyStruct{}
	err = json.Unmarshal(bodyBytes, b)
	if err != nil {
		log.Println(err)
	}
	// fmt.Println(b.Current.TempC)
	fmt.Println(b.Current.TempC)

	fmt.Println(string(bodyBytes))

}
