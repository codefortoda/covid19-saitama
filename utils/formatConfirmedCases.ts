type DataType = {
  attr: '検査実施人数'
  value: number
  children: [
    {
      attr: '陽性患者数'
      value: number
      children: [
        {
          attr: '入院中'
          value: number
          children: [
            {
              attr: '重症'
              value: number
            }
          ]
        },
        {
          attr: '宿泊療養'
          value: number
        },
        {
          attr: '自宅療養'
          value: number
        },
        {
          attr: '調整中'
          value: number
        },
        {
          attr: '死亡'
          value: number
        },
        {
          attr: '退院'
          value: number
        }
      ]
    }
  ]
}

type ConfirmedCasesType = {
  検査実施人数: number
  陽性患者数: number
  入院中: number
  重症: number
  宿泊療養: number
  自宅療養: number
  調整中: number
  死亡: number
  退院: number
}

export default (data: DataType) => {
  const formattedData: ConfirmedCasesType = {
    検査実施人数: data.value,
    陽性患者数: data.children[0].value,
    入院中: data.children[0].children[0].value,
    重症: data.children[0].children[0].children[0].value,
    宿泊療養: data.children[0].children[1].value,
    自宅療養: data.children[0].children[2].value,
    調整中: data.children[0].children[3].value,
    死亡: data.children[0].children[4].value,
    退院: data.children[0].children[5].value
  }
  return formattedData
}
