<template>
  <v-container>
    <v-layout row wrap>
      <v-flex md6>
        <v-card>
          <v-card-title>Hello World</v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam earum dolores
             quos fugiat delectus quisquam facilis. Quidem vitae nulla amet, necessitatibus et quae
             deleniti quod itaque blanditiis ex, alias similique, nesciunt omnis aliquam ratione
             ullam a exercitationem! Explicabo possimus voluptas consequuntur optio, nostrum voluptate
             modi quis in. Fugit corrupti eligendi nostrum. Deleniti itaque, nesciunt iure nisi ducimus
             voluptas blanditiis sed minima minus harum quo maiores esse. Aperiam cum, natus accusantium
             aspernatur excepturi, maiores, suscipit magnam debitis molestiae vitae mollitia. Placeat!
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn right flat color="teal lighten-2">Lorem</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
