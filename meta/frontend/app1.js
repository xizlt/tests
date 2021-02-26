const App1 = {
    data() {
        return {
            profiles: []
            name: 'Ctefan Grot',
            profile: 'fsdgfds'
        }
    },
    async created() {
        var response = await fetch('http://127.0.0.1:8000/api/v1/profile/')
        this.profiles = await response.json();
        console.log(this.profiles)
    }
}

Vue.createApp(App).mount('#app')