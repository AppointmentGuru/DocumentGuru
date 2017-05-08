<template>
  <div>
    <div>
      <el-input class="search" placeholder="Search by id ex 1" icon="search" v-model="input2" :on-icon-click="handleIconClick">
      </el-input>
    </div>
    <!--<strong>Todo</strong>
    <ul>
      <li>Ability to filter document list</li>
      <li>Ability to search document list</li>
    </ul>-->
  
    <strong>Listitem todo</strong>
    <ul>
      <li>Make it look nice</li>
    </ul>
      <el-popover ref="popover4" placement="right" width="510" trigger="click">
      <el-table :data="gridData">
        <el-table-column width="50" property="id" label="id"></el-table-column>
        <el-table-column width="145"property="name" label="name"></el-table-column>
        <el-table-column width="150" property="type" label="type"></el-table-column>
        <el-table-column width="150" property="url" label="URL" ></el-table-column>
      </el-table>
    </el-popover>
  
    <el-button class="documents" v-popover:popover4>Show Documents</el-button>
    <document-list-item v-for='document in documents' :key='document.id' :document='document' :repeat='document'>
    </document-list-item>
  </div>
</template>

<script>
  import DocumentListItem from './DocumentListItem'
  export default {
    name: 'DocumentList',
    components: {
      DocumentListItem
    },
    props: {
      documents: {
        type: Array,
        required: true
      }
    },
    data () {
      return {
        input2: '',
        gridData: [{
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
    methods: {
      handleIconClick (ev) {
        console.log(ev)
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
.search{
    margin: auto;
    width: 50%;
    padding: 10px;
}
</style>
