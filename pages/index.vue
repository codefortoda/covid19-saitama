<template>
  <div class="MainPage">
    <page-header
      :icon="'mdi-chart-timeline-variant'"
      :title="this.$t('都内の最新感染動向')"
      :date="Data.lastUpdate"
    />
    <whats-new class="mb-4" :items="newsItems" />
    <v-row class="DataBlock">
      <confirmed-cases-details-card />
      <confirmed-cases-number-card />
      <confirmed-cases-attributes-card />
      <confirmed-cases-by-municipalities-card />
      <inspection-summary-card />
    </v-row>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue'
import WhatsNew from '@/components/WhatsNew.vue'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/confirmed-cases-number-card.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/confirmed-cases-attributes-card.vue'
import ConfirmedCasesByMunicipalitiesCard from '@/components/cards/ConfirmedCasesByMunicipalitiesCard.vue'
import InspectionSummaryCard from '@/components/cards/InspectionSummaryCard.vue'
import Data from '@/data/data.json'
import News from '@/data/news.json'

export default {
  components: {
    PageHeader,
    WhatsNew,
    ConfirmedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    ConfirmedCasesByMunicipalitiesCard,
    InspectionSummaryCard
  },
  data() {
    const data = {
      Data,
      newsItems: News.newsItems
    }
    return data
  },
  head() {
    return {
      title: this.$t('都内の最新感染動向')
    }
  }
}
</script>

<style lang="scss" scoped>
.MainPage {
  .DataBlock {
    margin: 20px -8px;
    .DataCard {
      @include largerThan($medium) {
        padding: 10px;
      }
      @include lessThan($small) {
        padding: 4px 8px;
      }
    }
  }
}
</style>
