const App = {
  data() {
    return {
      // profiles: []
      profiles: [
        {
          "id": "rec3XvhYxD45RKTCe",
          "name": "Георгий",
          "photo": "https://dl.airtable.com/.attachments/c15cce685652a0670beb0f4bb2485041/0d0720fe/3.jpg",
          "methods": [
            {
              "id": 3,
              "title": "Сказкотерапия"
            },
            {
              "id": 1,
              "title": "Психоанализ"
            },
            {
              "id": 9,
              "title": "Музыкотерапия"
            }
          ]
        },
        {
          "id": "rec60Vls6AmXpYqGE",
          "name": "Иннокентий",
          "photo": "https://dl.airtable.com/.attachments/fa70928a82a214d22c4b7a2eeace79d2/e5a12360/2.jpg",
          "methods": [
            {
              "id": 3,
              "title": "Сказкотерапия"
            },
            {
              "id": 4,
              "title": "Гештальт-терапия"
            },
            {
              "id": 5,
              "title": "Коучинг"
            },
            {
              "id": 10,
              "title": "Психосинтез"
            }
          ]
        },
        {
          "id": "recLuzpKqfA0rA2RM",
          "name": "Василий",
          "photo": "https://dl.airtable.com/.attachments/7da0d4c7963babf742137abc4e9a1a99/5f547505/1.jpg",
          "methods": [
            {
              "id": 5,
              "title": "Коучинг"
            },
            {
              "id": 1,
              "title": "Психоанализ"
            },
            {
              "id": 9,
              "title": "Музыкотерапия"
            }
          ]
        },
        {
          "id": "reco2hGoswZcg4V6B",
          "name": "47",
          "photo": "https://dl.airtable.com/.attachments/2522cd129ab37f8827af7ab8bec0accc/7cca9a1a/3.jpg",
          "methods": [
            {
              "id": 5,
              "title": "Коучинг"
            }
          ]
        },
        {
          "id": "recr3qAnJo5J4WMpp",
          "name": "dfgdf",
          "photo": "https://dl.airtable.com/.attachments/7f31360968a449caadd7a66ee345a969/de50b113/3.jpg",
          "methods": []
        }
      ]
    }
  },
  // async created() {
  //   var response = await fetch('http://127.0.0.1:8000/api/v1/profile/')
  //   this.profiles = await response.json();
  //   console.log(this.profiles)
  // },
    }

Vue.createApp(App).mount('#app')