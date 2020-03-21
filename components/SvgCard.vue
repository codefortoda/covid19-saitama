<template>
  <data-view
    class="SvgCard"
    :title="title"
    :title-id="titleId"
    :date="date"
    :url="url"
  >
    <template v-slot:button>
      <p class="Graph-Desc">
        {{
          $t(
            '（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載'
          )
        }}<br />
        {{ $t('（県内市公表分やチャーター便帰国者を含む）') }}
      </p>
    </template>
    <slot />
  </data-view>
</template>

<i18n>
{
  "ja": {
    "（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載": "（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載",
    "（県内市公表分やチャーター便帰国者を含む）": "（県内市公表分やチャーター便帰国者を含む）"
  },
  "en": {
    "（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載": "(Note) This shows the examinations for the patients with possible infection or for those who had close contact with them.",
    "（県内市公表分やチャーター便帰国者を含む）": "(including Prefectural city announcement or the returnees on charter flights)"
  },
  "zh-cn": {
    "（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載": "（注）仅列出在东京都接受检查的疑似病例及确诊病例的密切接触者",
    "（県内市公表分やチャーター便帰国者を含む）": "（包括乘包机返日者等）"
  },
  "zh-tw": {
    "（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載": "（註）列出與東京都疑似病例或是曾與患者密切接觸 ",
    "（県内市公表分やチャーター便帰国者を含む）": "（包機返國者、郵輪乘客等除外）"
  },
  "ko": {
    "（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載": "（주）도내에서 의심 사례 또는 환자와 접속했을 가능성이 있는 사람으로서 검사를 실시한 것에 대해 게재.",
    "（県内市公表分やチャーター便帰国者を含む）": "（전세기 귀국자, 크루즈선 승객 등은 포함하지 않았습니다）"
  },
  "ja-basic": {
    "（注）県内において疑い例または患者の濃厚接触者として検査を行ったものについて掲載": "（ちゅうい）コロナ に かかっている かも しれない ひと、または コロナ の ひと と ちかく で たくさん はなした ひと に さいたまけん が けんさ した もの について かいています。",
    "（県内市公表分やチャーター便帰国者を含む）": "（さたまけん や まち が はっぴょう した ひと や にほん の くに が とくべつに おくった ひこうき で かえってきた ひと を ふくみます）"
  }
}
</i18n>

<style lang="scss" scoped>
.SvgCard {
  ::v-deep svg {
    width: 100%;
  }
  .Graph-Desc {
    margin-top: 10px;
    margin-bottom: 0;
    font-size: 12px;
    color: $gray-3;
  }
}
</style>

<script>
import DataView from '@/components/DataView.vue'

export default {
  components: { DataView },
  props: {
    title: {
      type: String,
      default: ''
    },
    titleId: {
      type: String,
      default: ''
    },
    date: {
      type: String,
      default: ''
    },
    url: {
      type: String,
      default: ''
    }
  }
}
</script>
