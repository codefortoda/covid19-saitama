<template>
  <v-col cols="12" md="6" class="DataCard">
    <svg-card
      :title="$t('検査陽性者の状況')"
      :title-id="'details-of-confirmed-cases'"
      :date="Data.patients.date"
      :url="'https://www.pref.saitama.lg.jp/a0701/covid19/jokyo.html'"
      :url-label="$t('出典：新型コロナウイルス感染症の県内の発生状況')"
    >
      <confirmed-cases-table
        :aria-label="$t('検査陽性者の状況')"
        v-bind="confirmedCases"
      />
    </svg-card>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatConfirmedCases from '@/utils/formatConfirmedCases'
import SvgCard from '@/components/SvgCard.vue'
import ConfirmedCasesTable from '@/components/ConfirmedCasesTable.vue'

export default {
  components: {
    SvgCard,
    ConfirmedCasesTable
  },
  data() {
    // 検査陽性者の状況
    const confirmedCases = formatConfirmedCases(Data.main_summary)

    const data = {
      Data,
      confirmedCases
    }
    return data
  }
}
</script>
