<template>
  <div id="app">
    <v-app id="app-container" dark>
      <img src="./assets/logo.png">
      <router-view/>
    </v-app>
    <v-footer class="pa-3" id="footer">
      <v-spacer></v-spacer><div>© Intraleagues {{ new Date().getFullYear() }}</div><v-spacer></v-spacer>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#footer{
  margin-top:1em;
}
</style>
