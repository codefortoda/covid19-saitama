<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-table
      :title="$t('陽性患者の属性')"
      :title-id="'attributes-of-confirmed-cases'"
      :chart-data="patientsTable"
      :chart-option="{}"
      :date="Data.patients.date"
      :info="sumInfoOfPatients"
      :url="'https://opendata.pref.saitama.lg.jp/data/dataset/covid19-jokyo'"
    />
  </v-col>
</template>

<script>
import DataTable from '@/components/DataTable.vue'
import formatGraph from '@/utils/formatGraph'
import formatTable from '@/utils/formatTable'
import Data from '@/data/data.json'

export default {
  components: {
    DataTable
  },
  data() {
    // 感染者数グラフ
    const patientsGraph = formatGraph(Data.patients_summary.data)
    // 陽性患者の属性
    const patientsTable = formatTable(Data.patients.data)

    //
    // ↓ は移植はしましたが、i18n対応が実質できていなくて不必要なのですが、一応持ってきています。
    //
    // // 陽性患者の属性 ヘッダー翻訳
    // for (const header of patientsTable.headers) {
    //   header.text =
    //     header.value === '退院' ? this.$t('退院※') : this.$t(header.value)
    // }
    // // 陽性患者の属性 中身の翻訳
    // for (const row of patientsTable.datasets) {
    //   row['居住地'] = this.$t(row['居住地'])
    //   row['性別'] = this.$t(row['性別'])

    //   if (row['年代'] === '10歳未満') {
    //     row['年代'] = this.$t('10歳未満')
    //   } else if (row['年代'].slice(-1) === '代') {
    //     const age = row['年代'].substring(0, 2)
    //     row['年代'] = this.$t('{age}代', { age })
    //   }
    // }

    let cnt = Data.patients.data.filter(function(x){return x.date==='調査中'}).length;

    const sumInfoOfPatients = {
      lText: (patientsGraph[
        patientsGraph.length - 1
      ].cumulative + cnt).toLocaleString(),
      sText: this.$t('{date}の累計', {
        date: patientsGraph[patientsGraph.length - 1].label
      }),
      unit: this.$t('人')
    }

    const data = {
      Data,
      patientsTable,
      sumInfoOfPatients
    }
    return data
  }
}
</script>
