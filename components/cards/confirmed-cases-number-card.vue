<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数')"
      :title-id="'number-of-confirmed-cases'"
      :chart-id="'time-bar-chart-patients'"
      :chart-data="patientsGraph"
      :date="Data.patients.date"
      :unit="$t('人')"
      :url="'https://opendata.pref.saitama.lg.jp/data/dataset/covid19-jokyo'"
      :option-count="optionCount"
    />
  </v-col>
</template>

<script>
import TimeBarChart from '@/components/TimeBarChart'
import formatGraph from '@/utils/formatGraph'
import Data from '@/data/data.json'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 感染者数グラフ
    const patientsGraph = formatGraph(Data.patients_summary.data)

    const optionCount = Data.patients.data.filter(function(x) {
      return x.date === '調査中'
    }).length

    const data = {
      Data,
      patientsGraph,
      optionCount
    }
    return data
  }
}
</script>
