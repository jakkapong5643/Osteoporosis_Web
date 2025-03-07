<template>
  <v-app>
    <v-app-bar color="teal lighten-1" dark app elevation="6">
      <v-toolbar-title class="white--text">
        <v-icon left>mdi-hospital-building</v-icon>
        Osteoporosis Prediction Application
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/" class="white--text">
        <v-icon left>mdi-home</v-icon>
        Home
      </v-btn>
      <v-btn text to="/inference" class="white--text">
        <v-icon left>mdi-bone</v-icon>
        Prediction
      </v-btn>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
.v-btn:hover {
  background-color: #00796b;
  transform: scale(1.05);
}
.v-icon {
  color: #ffffff;
}
</style>
