<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" md="8" lg="6">
        <v-card class="elevation-20 rounded-xl shadow-lg" color="#f5f5f5">
            <v-row align="center" justify="center" class="fill-height">
              <v-col class="text-center">
                <h1 class="white--text display-1 font-weight-bold">
                  Osteoporosis Prediction
                </h1>
                <p class="white--text subheading font-weight-medium">
                  Using an Accurate Machine Learning Model
                </p>
              </v-col>
            </v-row>
          <v-card-text class="text-center">
            <p class="mb-4 black--text font-weight-light">
              This application will help you quickly determine your risk of osteoporosis
            </p>
            <p class="black--text font-weight-normal">
              Start your prediction easily by clicking the button below!
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

