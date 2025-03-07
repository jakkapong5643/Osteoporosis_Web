<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>Osteoporosis Prediction</v-card-title>
          <v-card-text>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model.number="age"
                :rules="numberRules"
                label="Age"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="gender"
                :rules="numberRules"
                label="Gender"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="hormonalChanges"
                :rules="numberRules"
                label="Hormonal Changes"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="familyHistory"
                :rules="numberRules"
                label="Family History"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="raceEthnicity"
                :rules="numberRules"
                label="Race/Ethnicity"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="bodyWeight"
                :rules="numberRules"
                label="Body Weight"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="calciumIntake"
                :rules="numberRules"
                label="Calcium Intake"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="vitaminDIntake"
                :rules="numberRules"
                label="Vitamin D Intake"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="physicalActivity"
                :rules="numberRules"
                label="Physical Activity"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="smoking"
                :rules="numberRules"
                label="Smoking"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="alcoholConsumption"
                :rules="numberRules"
                label="Alcohol Consumption"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="medicalConditions"
                :rules="numberRules"
                label="Medical Conditions"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="medications"
                :rules="numberRules"
                label="Medications"
                required
              ></v-text-field>
              <v-text-field
                v-model.number="priorFractures"
                :rules="numberRules"
                label="Prior Fractures"
                required
              ></v-text-field>
            </v-form>
            <v-btn :disabled="!valid" color="primary" @click="predict">Predict</v-btn>
            <div v-if="prediction">
              <p>Prediction Result: {{ prediction.prediction }}</p>
              <p>Confidence: {{ prediction.confidence.toFixed(2)*100 }}%</p>
            </div>
            <div v-if="error">
              <p style="color: red;">Error: {{ error }}</p>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'InferencePage',
  data() {
    return {
      valid: true,
      age: null,
      gender: null,
      hormonalChanges: null,
      familyHistory: null,
      raceEthnicity: null,
      bodyWeight: null,
      calciumIntake: null,
      vitaminDIntake: null,
      physicalActivity: null,
      smoking: null,
      alcoholConsumption: null,
      medicalConditions: null,
      medications: null,
      priorFractures: null,
      numberRules: [
        (value) => !!value || 'Required',
        (value) => /^-?\d+(\.\d+)?$/.test(value) || 'Invalid number',
      ],
      prediction: null,
      error: null,
    };
  },
  methods: {
    async predict() {
      if (this.$refs.form.validate()) {
        const X_new = [
          this.age,
          this.gender,
          this.hormonalChanges,
          this.familyHistory,
          this.raceEthnicity,
          this.bodyWeight,
          this.calciumIntake,
          this.vitaminDIntake,
          this.physicalActivity,
          this.smoking,
          this.alcoholConsumption,
          this.medicalConditions,
          this.medications,
          this.priorFractures,
        ];
        try {
          const response = await axios.post('http://127.0.0.1:8000/predict/', { X_new });
          this.prediction = response.data;
          this.error = null;
        } catch (error) {
          console.error(error);
          this.error = error.message || 'Error Prediction';
          this.prediction = null;
        }
      }
    },
  },
};
</script>
