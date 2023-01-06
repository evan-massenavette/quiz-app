<template>
  <v-table fixed-header density="comfortable" id="score_table">
    <thead>
      <tr>
        <th class="text-center font-weight-bold rank_column">Rank</th>
        <th class="font-weight-bold">Player</th>
        <th class="font-weight-bold">Score</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in scoresAndRanks" :key="item.playerName"
        :id="item.rank == highlightedRank ? 'rank_one_row' : ''">
        <td class="text-center rank_column">{{ item.rank }}</td>
        <td>{{ item.playerName }}</td>
        <td>{{ item.score }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
export default {
  name: "HomePage",
  props: {
    highlightedRank: {
      type: Number,
      default: 1,
    },
    scoresAndRanks: {
      type: Array,
      default: (rawProps) => [],
      validator: (value) => {
        const neededKeys = ['playerName', 'score', 'rank']

        // Function to check that object has certain keys
        const hasAllKeys = (obj, keys) => keys.every(key => obj.hasOwnProperty(key));

        // Check that every object inside value has all the needed keys
        const isValid = value.every(element => hasAllKeys(element, neededKeys));

        if (!isValid) {
          console.warn(`Every object in the 'scoresAndRanks' array needs to 
          have the following keys : ${neededKeys.join(', ')}`)
        }

        return isValid;
      }
    }
  },
};
</script>

<style scoped>
thead {
  font-weight: bolder;
}

.rank_column {
  width: 50px;
}

#rank_one_row {
  color: rgb(var(--v-theme-accent));
}
</style>