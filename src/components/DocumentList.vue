<template>
<el-row :gutter="20">
  <el-col :span="16">
  <div class="documentList">
    <h3>Document List</h3>
    <div>
      <el-input class="search" placeholder="Search by id ex 1" icon="search" v-model="filterText" :on-icon-click="handleIconClick">
      </el-input>
    </div>
    <ul>
      <li v-for="Datas in Data">
       {{ Datas.name }} - {{ Datas.type }} - {{ Datas.url }}
      </li>
    </ul>
    <p> {{ ev }} </p>
  </div>
  </el-col>
  </el-row>
</template>

<script>
  import DocumentListItem from './DocumentListItem'
  export default {
    name: 'DocumentList',
    components: {
      DocumentListItem
    },
    data () {
      return {
        filterText: '',
        Data: [{
          id: 1,
          name: 'A name describing this file',
          type: 'application/pdf',
          url: 'http://someplace.com/foo'
        },
        {
          id: 2,
          name: 'A different name describing this file',
          type: 'application/pdf',
          url: 'http://someplace.com/foo'
        }
        ]
      }
    },
    computed: {
      filterdData () {
        return this.Data.filter((element) => {
          return element.match(this.filterText)
        })
      }
    },
    methods: {
      handleIconClick (ev) {
        console.log(ev)
        return this.ev
      }
    }
  }
</script>

<style>
.documents {
  background-color:orangered;
  -webkit-text-fill-color: black;
  margin: auto;
  padding: 10px;
}
  .el-row {
    margin-bottom: 20px;
  }
  .el-col {
    border-radius: 4px;
  }
  .documentList{
    border-style: solid;
    border-width: 0.5px;
  }
</style>
