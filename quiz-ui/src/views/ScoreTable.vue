<template>
  <v-table fixed-header density="comfortable">
    <thead>
      <tr>
        <th class="text-center font-weight-bold rank_column">Rank</th>
        <th class="font-weight-bold">Player</th>
        <th class="font-weight-bold">Score</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in tempScoresAndRanks" :key="item.playerName">
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
    scoresAndRanks: {
      type: Array,
      default: (rawProps) => [],
      validator: (value) => {
        const neededKeys = ['playerName', 'score', 'rank'].join(', ')

        // Function to check that object has certain keys
        const hasAllKeys = (obj, keys) => keys.every(key => obj.hasOwnProperty(key));

        // Check that every object inside value has all the needed keys
        const isValid = value.every(element => hasAllKeys(element, neededKeys));

        if (!isValid) {
          console.warn(`Every object in the scoresAndRanks array needs to 
          have the following keys : ${neededKeys.join(', ')}`)
        }

        return isValid;
      }
    }
  },
  data() {
    return {
      tempScoresAndRanks: [
        {
          playerName: 'Frozen Yogurt',
          score: 159,
          rank: 2,
        },
        {
          playerName: 'Ice cream sandwich',
          score: 237,
          rank: 4,
        },
        {
          playerName: 'Eclair',
          score: 262,
          rank: 6,
        },
        {
          playerName: 'Cupcake',
          score: 305,
          rank: 8,
        },
        {
          playerName: 'Gingerbread',
          score: 356,
          rank: 1,
        },
        {
          playerName: 'Jelly bean',
          score: 375,
          rank: 3,
        },
        {
          playerName: 'Lollipop',
          score: 392,
          rank: 5,
        },
        {
          playerName: 'Honeycomb',
          score: 408,
          rank: 7,
        },
        {
          playerName: 'Donut',
          score: 452,
          rank: 9,
        },
        {
          playerName: 'KitKat',
          score: 518,
          rank: 10,
        },
      ]
    };
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

tbody:first-child {
  color: rgb(var(--v-theme-accent))
}
</style>