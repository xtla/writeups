### Steps
* Reversed the code and checked which functions were called from libraries
* Found that some unknown x is checked, which a formula `x^a % b = c`, where a, b, c are known values
* Used [wolfram alpha](https://www.wolframalpha.com/input?i=%28%28x+%5E+61651%29+modulo+38830568246783%29+%3D+17475150661108) to solve the 10 equations


### cap function
```c
void cap(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)

{
  long lVar1;
  long in_FS_OFFSET;
  undefined4 local_2c;
  undefined local_28 [24];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_2c = 0x2a4e700f;
                    /* __gmpz_set_ui */
  ResolveModuleFunction(param_2,0xf122f362,param_4,0);
                    /* hcreate */
  ResolveModuleFunction(param_1,0xe75e0ffe,param_3);
                    /* memfrob */
  ResolveModuleFunction(param_1,0x1c46d38a,&local_2c,4);
  do {
                    /* __gmp_sprintf */
    ResolveModuleFunction(param_2,0x7489af98,local_28,&local_2c,param_4);
                    /* __gmpz_add_ui */
    ResolveModuleFunction(param_2,0xed3b7a10,param_4,param_4,1);
                    /* hsearch */
    lVar1 = ResolveModuleFunction(param_1,0x50ab4097,local_28,0,1);
  } while (lVar1 != 0);
                    /* hdestroy */
  ResolveModuleFunction(param_1,0xaf4c09bd);
                    /* __gmpz_sub_ui */
  ResolveModuleFunction(param_2,0x1c3ef940,param_4,param_4,1);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
  }
  return;
}
```

### main function
```c
undefined8 main(int param_1,undefined8 *param_2)

{
  int iVar1;
  undefined8 uVar2;
  size_t sVar3;
  long lVar4;
  long lVar5;
  long in_FS_OFFSET;
  ulong local_80;
  ulong index;
  ulong local_70;
  undefined base [16];
  undefined modulo [16];
  undefined exp [24];
  long local_10;
  char *input_string;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 < 2) {
    printf("Usage: %s FLAG\n",*param_2);
    uVar2 = 1;
    goto LAB_00101d61;
  }
  input_string = (char *)param_2[1];
  sVar3 = strlen(input_string);
  if (sVar3 != 0x28) {
    puts("Nowhere near close.");
    uVar2 = 0;
    goto LAB_00101d61;
  }
  lVar4 = LoadLibraryA("libc.so.6");
  if (lVar4 == 0) {
    __assert_fail("hLibc != NULL","main.c",0x4a,(char *)&__PRETTY_FUNCTION__.0);
  }
  lVar5 = LoadLibraryA("libgmp.so");
  if (lVar5 == 0) {
    __assert_fail("hGMP != NULL","main.c",0x4c,(char *)&__PRETTY_FUNCTION__.0);
  }
                    /* __gmpz_init */
  ResolveModuleFunction(lVar5,0x71b5428d,base);
                    /* __gmpz_init */
  ResolveModuleFunction(lVar5,0x71b5428d,modulo);
                    /* __gmpz_init */
  ResolveModuleFunction(lVar5,0x71b5428d,exp);
                    /* srandom */
  ResolveModuleFunction(lVar4,0xfc7e7318,_main);
                    /* setbuf */
  ResolveModuleFunction(lVar4,0x9419a860,stdout,0);
  printf("Checking...");
  for (local_80 = 0; local_80 < 0x28; local_80 = local_80 + 1) {
                    /* isprint */
    iVar1 = ResolveModuleFunction(lVar4,0x4e8a031a,(int)input_string[local_80]);
    if (iVar1 == 0) goto LAB_00101ce7;
  }
  for (index = 0; index < 0x28; index = index + 4) {
                    /* __gmpz_set_ui */
    ResolveModuleFunction(lVar5,0xf122f362,modulo,1);
    for (local_70 = 0; local_70 < 3; local_70 = local_70 + 1) {
                    /* putchar */
      ResolveModuleFunction(lVar4,0xd588a9,0x2e);
                    /* rand */
      iVar1 = ResolveModuleFunction(lVar4,0x7b6cea5d);
      cap(lVar4,lVar5,(long)(iVar1 % 0x10000),base);
                    /* __gmpz_mul */
      ResolveModuleFunction(lVar5,0x347d865b,modulo,modulo,base);
    }
                    /* putchar */
    ResolveModuleFunction(lVar4,0xd588a9,0x2e);
                    /* rand */
    iVar1 = ResolveModuleFunction(lVar4,0x7b6cea5d);
    cap(lVar4,lVar5,(long)(iVar1 % 0x10000),exp);
                    /* __gmpz_set_ui */
    ResolveModuleFunction(lVar5,0xf122f362,base,*(undefined4 *)(input_string + index));
                    /* __gmpz_powm */
    ResolveModuleFunction(lVar5,0x9023667e,base,base,exp,modulo);
                    /* __gmpz_cmp_ui */
    iVar1 = ResolveModuleFunction(lVar5,0xb1f820dc,base,*(undefined8 *)(encoded + (index >> 2) * 8))
    ;
    if (iVar1 != 0) goto LAB_00101ce7;
  }
  puts("\nCorrect!");
  goto LAB_00101cf6;
LAB_00101ce7:
  puts("\nWrong.");
LAB_00101cf6:
  ResolveModuleFunction(lVar5,0x31cc4f9f,base);
  ResolveModuleFunction(lVar5,0x31cc4f9f,modulo);
  ResolveModuleFunction(lVar5,0x31cc4f9f,exp);
  CloseHandle(lVar4);
  CloseHandle(lVar5);
  uVar2 = 0;
LAB_00101d61:
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return uVar2;
  }
  __stack_chk_fail();
}
```
