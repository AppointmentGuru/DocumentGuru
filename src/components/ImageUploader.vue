<style>
  .upload-demo .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .upload-demo .el-upload:hover {
    border-color: #20a0ff;
  }
  .upload-demo-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px !important;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
    .el-row {
    margin-bottom: 20px;
    border: 1px;

  }
  .el-col {
    border-radius: 4px;

  }
  .grid-content {
    border-style: solid;
    border-width: 0.5px;
  }
</style>
<template>
<el-row :gutter="20">
  <el-col :span="7">
<div class="grid-content">
  <h4>Choose a file type!</h4>
  <el-dropdown>
  <el-button type="primary">
    Dropdown List<i class="el-icon-caret-bottom el-icon--right"></i>
  </el-button>
  <el-dropdown-menu slot="dropdown">
    <el-dropdown-item>ID Photo</el-dropdown-item>
    <el-dropdown-item>Drivers Licence</el-dropdown-item>
    <el-dropdown-item>Sick Note</el-dropdown-item>
    <el-dropdown-item>Avetar Photo</el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>

<el-upload
  class="upload-demo"
  drag
  action="https://jsonplaceholder.typicode.com/posts/"
  :on-preview="handlePreview"
  :on-remove="handleRemove"
  :before-upload="beforeAvatarUpload"
  :file-list="fileList2"
  list-type="picture">
   <i class="el-icon-upload"></i>
  <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
  <div slot="tip" class="el-upload__tip">jpg file with a size less than 500kb</div>
</el-upload>
</div>
</el-col>
</el-row>
</template>
<script>
  export default {
    data: function () {
      return {
        fileList2: [

        ]
      }
    },
    methods: {
      handleRemove (file, fileList) {
        console.log(file, fileList)
      },
      handlePreview (file) {
        console.log(file)
      },
      beforeAvatarUpload (file) {
        const isLt2M = file.size / 500 / 500 < 2
        if (!isLt2M) {
          alert('Picture size can not exceed 2MB!')
        }
        return isLt2M
      }
    }
  }
</script>
